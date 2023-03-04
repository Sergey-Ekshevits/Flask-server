import { useContext, useState } from "react"
import { validateEmail } from "../utils"
import { observer } from "mobx-react"
import {useStore} from "../store/context"
export const LoginForm = observer(() => {
    const userStore = useStore((state) => state.userStore);
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const handleSubmit = async (e) => {
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
            setEmail("")
            setPassword("")
        } catch (error) {
            console.log(error);
        }
    }
    return (
        <form onSubmit={handleSubmit} className="registrate-form">
            LOGIN
            <label>
                <span>Email</span>
                <input value={email} onChange={(e) => setEmail(e.target.value)} />
                {/* <TextField id="outlined-basic" label="Outlined" variant="outlined" /> */}
            </label>
            <label>
                <span>Password</span>
                <input value={password} onChange={(e) => setPassword(e.target.value)} />
            </label>

            <button>Отправить</button>
        </form>
    )
})