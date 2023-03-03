import { useContext, useState } from "react"
import { validateEmail } from "../utils"
import { observer } from "mobx-react"
import User from "../store/User"
export const LoginForm = observer(() => {
    const userState = useContext(User)
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
            await userState.login(email, password)
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
            </label>
            <label>
                <span>Password</span>
                <input value={password} onChange={(e) => setPassword(e.target.value)} />
            </label>

            <button>Отправить</button>
        </form>
    )
})