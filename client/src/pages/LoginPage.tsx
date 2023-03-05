import React from "react"
import { Container } from "@mui/material"
import { LoginForm } from "../components/LoginForm"
import { Typography } from '@mui/material';
import { useNavigate } from "react-router-dom";

export const LoginPage = () => {
    const navigate = useNavigate();
    const authSuccess = () => navigate("/")
    return (
        <Container maxWidth="md">
            <Typography mt={2} textAlign="center">Аутификация</Typography>
            <LoginForm authSuccess={authSuccess} />
        </Container>
    )
}