import { Box, Button, Grid, TextField, Typography } from "@mui/material"
import Container from "@mui/material/Container"
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { EmptyPicture } from "../components/EmptyPicture";


export const ProfilePage = () => {
    const [image, setImage] = useState<null | string>("")
    const [imageToSend, setImageToSend] = useState<null | string>("")

    const navigate = useNavigate();
    const handleFile = (e: any) => {
        console.log(e);
        const file = e.target.files[0]
        setImageToSend(file)
        getBase64(file)
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
            return <EmptyPicture height={"194"} />
        }
        return (
            <img src={image} style={{ maxHeight: "500px", maxWidth: "100%", objectFit: "cover" }} />
        )
    }
    return (
        <Container maxWidth="md">
            <Typography mt={2} textAlign="center">ProfilePage</Typography>

            <Grid mt={2} container spacing={2} sx={{ alignContent: "stretch" }}>

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
                    <Box mt={1} component="form" onSubmit={() => { }} className="form">
                        <TextField
                            margin="dense"
                            value={"name"}
                            // onChange={(e) => setName(e.target.value)}
                            type="text"
                            id="outlined-basic"
                            label="Name"
                            variant="outlined"
                            size="small"
                        />
                        <TextField
                            margin="dense"
                            value={"email"}
                            // onChange={(e: any) => setEmail(e.target.value)}
                            type="email"
                            id="outlined-basic"
                            label="Email"
                            variant="outlined"
                            size="small"
                        />
                        <TextField
                            margin="dense"
                            value={"password"}
                            // onChange={(e: any) => setPassword(e.target.value)}
                            type="password"
                            id="outlined-basic"
                            label="password"
                            variant="outlined"
                            size="small"
                        />
                        <TextField
                            margin="dense"
                            value={"repeatPassword"}
                            // onChange={(e) => setRepeatPassword(e.target.value)}
                            type="password"
                            id="outlined-basic"
                            label="Repeat password"
                            variant="outlined"
                            size="small"
                        />
                        <Box mt={2}>
                            <Button size="small" variant="contained" type="submit">Сохранить</Button>
                        </Box>
                    </Box>
                </Grid>
            </Grid>
        </Container>
    )
}