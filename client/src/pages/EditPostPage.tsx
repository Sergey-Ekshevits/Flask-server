import { Box, Button, Container, Grid, TextField, Typography } from "@mui/material";
import { observer } from "mobx-react";
import React, { useEffect, useState } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import { useParams } from "react-router-dom";
import Editor from "../components/Editor";
import { EmptyPicture } from "../components/EmptyPicture";
import { STATIC_AVATAR_URL, STATIC_POST_URL } from "../constant";
import { ALERT_EVENT, useAppContext, useEventAlert } from "../contexts/AppContext";
import { useStore } from "../store/context";
import { PostDto } from "../types";

interface CreatePostPageProps {

}

const CreatePostPage = observer(({ }: CreatePostPageProps) => {
    const postStore = useStore((state) => state.postStore);
    const eventAlert = useEventAlert()
    const [body, setBody] = useState("");
    const [title, setTitle] = useState("");
    const [image, setImage] = useState<string | null>(null);
    const [hasChanges, setHasChanges] = useState(false);
    const [imageToSend, setImageToSend] = useState<null | File>(null)

    const { id } = useParams();

    useEffect(() => {
        postStore.getPost(id).then((post: PostDto) => {
            setPost(post)
        })
    }, [])


    const setPost = (post: PostDto) => {
        setBody(post?.body)
        setTitle(post?.title)
        post?.post_pic && setImage(post?.post_pic)
    }

    const onSubmit = async () => {
        if (!body || !title) {
            eventAlert({
                message: "Нужно заполнить поля!",
                type: "error"
            })
        }

        const post = await postStore.updatePost(id, title, body, imageToSend)
        if (postStore.status === "success") {
            eventAlert({
                message: "Пост обновлен!",
                type: "success"
            })
            setImageToSend(null)
            setHasChanges(false)
            setPost(post)
        }
    }

    const handleFile = (e: any) => {
        const file = e.target.files[0]
        setImageToSend(file)
        getBase64(file)
        setHasChanges(true)
    }

    const getBase64 = (file: any) => {
        let reader = new FileReader()
        if (!file) {
            return;
        }
        reader.readAsDataURL(file)
        reader.onload = () => {
            setImage(reader.result as string)
        };
        reader.onerror = function (error) {
            console.log('Error: ', error);
        }
    }

    const onChange = (value: string, cb: (value: string) => void) => {
        cb(value)
        setHasChanges(true)
    }

    const renderPicture = () => {
        if (!image) {
            return <EmptyPicture height={"194"} />
        }
        if (imageToSend) {
            return (
                <img src={image}
                    style={{ maxHeight: "300px", maxWidth: "100%", objectFit: "contain" }} />

            )
        }
        return (
            <img src={STATIC_POST_URL + "\\" + image}
                style={{ maxHeight: "300px", maxWidth: "100%", objectFit: "contain" }} />
        )
    }


    return (
        <Container maxWidth="md">
            <Grid mt={2} container spacing={2} sx={{ alignContent: "stretch" }}>
                <Grid item xs={12} sm={6} md={6} lg={6} xl={6}>
                    <Typography variant={"h5"}>Редактирование поста</Typography>

                </Grid>
                <Grid item xs={12} sm={6} md={6} lg={6} xl={6} >
                    {hasChanges && <Button
                        onClick={onSubmit}
                        sx={{ marginLeft: "auto", display: "flex" }}
                        variant="contained"
                    >
                        Сохранить
                    </Button>}
                </Grid>
            </Grid>

            <TextField
                margin="dense"
                value={title}
                onChange={(e) => onChange(e.target.value, setTitle)}
                type="text"
                id="outlined-basic"
                label="Заголовок"
                variant="outlined"
                size="small"
            />
            <Box mt={1}>
                <Editor value={body} setValue={(value: string) => {
                    setBody(value)
                    setHasChanges(true)
                    // onChange(value, )
                }} />
            </Box>
            <Box mt={2}>
                {renderPicture()}
            </Box>
            <Box mt={2} mb={5}>
                <Button
                    variant="contained"
                    component="label"
                >
                    Загрузить файл
                    <input
                        onChange={handleFile}
                        type="file"
                        hidden
                    />
                </Button>
            </Box>
        </Container>
    );
})

export default CreatePostPage;