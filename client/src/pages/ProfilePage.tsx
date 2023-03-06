import {Box, Button, Grid, TextField, Typography} from "@mui/material"
import Container from "@mui/material/Container"
import {observer} from "mobx-react";
import {useState} from "react";
import {useNavigate} from "react-router-dom";
import EditableText from "../components/EditableText";
import {EmptyPicture} from "../components/EmptyPicture";
import {useStore} from "../store/context";
import {STATIC_AVATAR_URL} from "../constant";


export const ProfilePage = observer(() => {
    const user = useStore((state) => state.userStore.user);
    const [image, setImage] = useState<null | string>(user?.avatar_url ?? "")
    const [hasChanges, setHasChanges] = useState<boolean>(false)
    const [name, setName] = useState<null | string>(user?.name ?? "")
    const [email, setEmail] = useState<null | string>(user?.email ?? "")
    const [imageToSend, setImageToSend] = useState<null | File>(null)

    const navigate = useNavigate();
    const handleFile = (e: any) => {
        console.log(e);
        const file = e.target.files[0]
        setImageToSend(file)
        getBase64(file)
        setHasChanges(true)
    }


    const onSubmit = () => {
        //         name
        // email
        // imageToSend
        setHasChanges(false)
    }

    const onChangeName = (name: string) => {
        setHasChanges(true)
        setName(name)
    }

    const onChangeEmail = (name: string) => {
        setHasChanges(true)
        setEmail(name)
    }


    const onRefresh = () => {
        setImage(user?.avatar_url ?? "")
        setName(user?.name ?? "")
        setEmail(user?.email ?? "")
        setImageToSend(null)
        setHasChanges(false)
    }

    const getBase64 = (file: any) => {
        let reader = new FileReader()
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
            return <EmptyPicture height={"194"}/>
        }
        if (imageToSend) {
            return (
                <img src={image}
                     style={{maxHeight: "300px", maxWidth: "100%", objectFit: "contain"}}/>

            )
        }
        return (
            <img src={STATIC_AVATAR_URL + "\\" + image}
                 style={{maxHeight: "300px", maxWidth: "100%", objectFit: "contain"}}/>
        )
    }
    return (
        <Container maxWidth="md">
            <Typography mt={2} textAlign="center">ProfilePage</Typography>

            <Grid mt={2} container spacing={2} sx={{alignContent: "stretch"}}>

                <Grid item xs={12} sm={6} md={6} lg={6} xl={6}>
                    {renderPicture()}
                    <Box mt={2}>
                        <Button
                            variant="contained"
                            component="label"
                        >
                            Upload File
                            <input
                                onChange={handleFile}
                                type="file"
                                hidden
                            />
                        </Button>
                    </Box>
                </Grid>

                <Grid item xs={12} sm={6} md={6} lg={6} xl={6}>
                    <Box onSubmit={() => {
                    }}>
                        <EditableText value={name} title={"Имя"} onEdit={onChangeName}/>
                        <EditableText value={email} title={"E-mail"} onEdit={onChangeEmail}/>

                        {/* <TextField
                            margin="dense"
                            value={"password"}
                            // onChange={(e: any) => setPassword(e.target.value)}
                            type="password"
                            id="outlined-basic"
                            label="password"
                            variant="outlined"
                            size="small"
                        /> */}

                        {hasChanges && (
                            <Box sx={{justifyContent: "space-between", display: "flex"}} mt={2}>
                                <Button onClick={onRefresh} size="small" variant="contained"
                                        type="button">Сбросить</Button>
                                <Button
                                    onClick={onSubmit}
                                    size="small"
                                    variant="contained"
                                    type="button">Сохранить</Button>
                            </Box>
                        )}
                    </Box>
                </Grid>
            </Grid>
        </Container>
    )
})