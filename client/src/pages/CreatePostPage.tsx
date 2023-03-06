import { Box, Button, Container, Grid, TextField, Typography } from "@mui/material";
import React, { useState } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import Editor from "../components/Editor";
import { EmptyPicture } from "../components/EmptyPicture";
import { STATIC_AVATAR_URL } from "../constant";
import { ALERT_EVENT, useAppContext, useEventAlert } from "../contexts/AppContext";
import { useStore } from "../store/context";

interface CreatePostPageProps {

}

const CreatePostPage = ({ }: CreatePostPageProps) => {
    const postStore = useStore((state) => state.postStore);
    const eventAlert = useEventAlert()

    const [value, setValue] = useState('');
    const [title, setTitle] = useState('');
    const [image, setImage] = useState('');
    const [hasChanges, setHasChanges] = useState(false);
    const [imageToSend, setImageToSend] = useState<null | File>(null)

    const onSubmit = () => {
        if (!value || !title || !imageToSend) {
            eventAlert({
                message: "Нужно заполнить поля!",
                type: "error"
            })
        }

        setHasChanges(false)
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

    const renderPicture = () => {
        if (!image) {
            return <EmptyPicture height={"194"} />
        }
        return (
            <img src={image}
                style={{ maxHeight: "300px", maxWidth: "100%", objectFit: "contain" }} />
        )
    }


    return (
        <Container maxWidth="md">
            <Grid mt={2} container spacing={2} sx={{ alignContent: "stretch" }}>
                <Grid item xs={12} sm={6} md={6} lg={6} xl={6}>
                    <Typography variant={"h5"}>Создание поста</Typography>

                </Grid>
                <Grid item xs={12} sm={6} md={6} lg={6} xl={6} >
                    <Button
                        onClick={onSubmit}
                        sx={{ marginLeft: "auto", display: "flex" }}
                        variant="contained"
                    >
                        Сохранить
                    </Button>
                </Grid>
            </Grid>

            <TextField
                margin="dense"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                type="text"
                id="outlined-basic"
                label="Заголовок"
                variant="outlined"
                size="small"
            />
            <Box mt={1}>
                <Editor value={value} setValue={setValue} />
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
}

export default CreatePostPage;