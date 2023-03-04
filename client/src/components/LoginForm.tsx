import { useState } from "react"
import { validateEmail } from "../utils"
import { observer } from "mobx-react"
import { useStore } from "../store/context"
import TextField from "@mui/material/TextField"
import React from "react"
import Button from "@mui/material/Button"
import Box from "@mui/material/Box"

type Props = {
    authSuccess: () => void
}
export const LoginForm = observer(({ authSuccess: loginSuccess }: Props) => {
    const userStore = useStore((state) => state.userStore);
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const handleSubmit = async (e: any) => {
        e.preventDefault();

        if (
            !email ||
            !password
        ) {
            alert("ЗАполни все поля!!")
            return
        }
        if (!validateEmail(email)) {
            alert("Нужно ввести корректный email!")
            return
        }
        try {
            await userStore.login(email, password)
            loginSuccess()
            setEmail("")
            setPassword("")
        } catch (error) {
            console.log(error);
        }
    }
    return (
        <Box mt={1} component="form" onSubmit={handleSubmit} className="form">
            <TextField
                margin="dense"
                value={email}
                onChange={(e: any) => setEmail(e.target.value)}
                type="email"
                id="outlined-basic"
                label="Email"
                variant="outlined"
                size="small"
            />
            <TextField
                margin="dense"
                value={password}
                onChange={(e: any) => setPassword(e.target.value)}
                type="password"
                id="outlined-basic"
                label="password"
                variant="outlined"
                size="small"
            />
            <Box mt={2}>
                <Button size="small" variant="contained" type="submit">Отправить</Button>
            </Box>
        </Box>
    )
})