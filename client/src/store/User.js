import { makeAutoObservable } from "mobx"
import { createContext } from "react"
import { restService } from "../services/RestService"

const KEY_USER = "KEY_USER"
class User {
    id = Math.random()
    user = null
    finished = false
    access_token = null

    constructor() {
        makeAutoObservable(this)
        this.init();
    }

    registrate(name,
        email,
        password,
        repeatPassword) {
        const response = restService.post("/registrate", JSON.stringify({
            name,
            email,
            password,
            repeatPassword,
        })).then((res) => res.json()).catch((err) => console.log(err))
        return response;
    }

    async login(email, password) {
        const response = restService.post("/login", JSON.stringify({
            email,
            password,
        })).then((res) => res.json())

        this.access_token = response.access_token
        this.user = response.user
        localStorage.setItem(KEY_USER, JSON.stringify({ access_token: response.access_token, user: response.user }))
        // this.finished = !this.finished
    }

    init() {
        let response = localStorage.getItem(KEY_USER)
        if (response) {
            response = JSON.parse(response)
            console.log(response);
            this.access_token = response.access_token
            this.user = response.user
        }

    }
}
export const userStore = new User()
export default createContext(userStore)