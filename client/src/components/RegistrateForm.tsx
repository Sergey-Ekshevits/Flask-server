import { useState, useContext } from "react"
import { validateEmail } from "../utils"
import { observer } from "mobx-react"
import { useStore } from '../store/context';
import { Box, TextField, Button } from "@mui/material";
import { useEventAlert } from "../contexts/AppContext";
type Props = {
    authSuccess: () => void
}
export const RegistrateForm = observer(({ authSuccess }: Props) => {
    const userStore = useStore((state) => state.userStore);
    const eventAlert = useEventAlert();
    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [repeatPassword, setRepeatPassword] = useState("")
    const handleSubmit = async (e: any) => {
        e.preventDefault();
        if (
            !name ||
            !email ||
            !password ||
            !repeatPassword
        ) {
            eventAlert({
                message: "Нужно заполнить все поля!",
                type: "error"
            })
            return
        }
        if (!validateEmail(email)) {
            eventAlert({
                message: "Нужно ввести корректный email!",
                type: "error"
            })
            return
        }
        if (password !== repeatPassword) {
            eventAlert({
                message: "Пароли не совадают",
                type: "error"
            })
            return
        }
        try {
            const response = await userStore.registrate(name,
                email,
                password,
                repeatPassword)
            setName("")
            setEmail("")
            setPassword("")
            setRepeatPassword("")
            authSuccess();
        } catch (error) {
            console.log(error);
        }
    }
    return (

        <Box mt={1} component="form" onSubmit={handleSubmit} className="form">
            <TextField
                margin="dense"
                value={name}
                onChange={(e) => setName(e.target.value)}
                type="text"
                id="outlined-basic"
                label="Name"
                variant="outlined"
                size="small"
            />
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
            <TextField
                margin="dense"
                value={repeatPassword}
                onChange={(e) => setRepeatPassword(e.target.value)}
                type="password"
                id="outlined-basic"
                label="Repeat password"
                variant="outlined"
                size="small"
            />
            <Box mt={2}>
                <Button size="small" variant="contained" type="submit">Отправить</Button>
            </Box>
        </Box>
    )
})