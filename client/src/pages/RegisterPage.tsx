import { Typography } from "@mui/material"
import Container from "@mui/material/Container"
import { useNavigate } from "react-router-dom";
import { RegistrateForm } from "../components/RegistrateForm"


export const RegisterPage = () => {
    const navigate = useNavigate();
    const authSuccess = () => navigate("/")
    return (
        <Container maxWidth="md">
             <Typography mt={2} textAlign="center">Регистрация</Typography>
            <RegistrateForm authSuccess={authSuccess} />
        </Container>
    )
}