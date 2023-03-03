import { useState } from "react"
import { validateEmail } from "../utils"
import { observer } from "mobx-react"
export const RegistrateForm = observer(() => {
    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [repeatPassword, setRepeatPassword] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (
            !name ||
            !email ||
            !password ||
            !repeatPassword
        ) {
            alert("ЗАполни все поля!!")
            return
        }
        if (!validateEmail(email)) {
            alert("Нужно ввести корректный email!")
            return
        }
        if (password !== repeatPassword) {
            alert("пароли не совадают")
            return
        }
        try {
            const response = await fetch("http://192.168.1.34:5000/api/registrate", {
                method: "POST",
                headers: {
                    "Content-type": "application/json"
                },
                body: JSON.stringify({
                    name,
                    email,
                    password,
                    repeatPassword
                })
            }).then((res) => res.json())
            console.log(response);
            setName("")
            setEmail("")
            setPassword("")
            setRepeatPassword("")
        } catch (error) {
            console.log(error);
        }
    }
    return (
        <form onSubmit={handleSubmit} className="registrate-form">
            <label>
                <span>Name</span>
                <input value={name} onChange={(e) => setName(e.target.value)} />
            </label>
            <label>
                <span>Email</span>
                <input value={email} onChange={(e) => setEmail(e.target.value)} />
            </label>
            <label>
                <span>Password</span>
                <input value={password} onChange={(e) => setPassword(e.target.value)} />
            </label>
            <label>
                <span> Repeat Password</span>
                <input value={repeatPassword} onChange={(e) => setRepeatPassword(e.target.value)} />
            </label>
            <button>Отправить</button>
        </form>
    )
})