import { makeAutoObservable } from "mobx"
import { restService } from "../services/RestService"

const KEY_USER = "KEY_USER"
export class UserStore {
    user = null
    access_token = null
    status = ""
    errorMessage = ""

    constructor() {
        makeAutoObservable(this)
        this.init();
    }

    registrate(name,
        email,
        password,
        repeatPassword) {

        try {
            this.status = "loading"
            const response = restService.post("/registrate", JSON.stringify({
                name,
                email,
                password,
                repeatPassword,
            })).then((res) => res.json())
            this.access_token = response.access_token
            this.user = response.user
            localStorage.setItem(KEY_USER, JSON.stringify({ access_token: response.access_token, user: response.user }))
            this.status = "done"
        } catch (err) {
            console.log({ err });
            this.status = "error"
            this.errorMessage = err
        }
    }

    async login(email, password) {
        try {
            this.status = "loading"
            const response = await restService.post("/login", JSON.stringify({
                email,
                password,
            })).then((res) => res.json())
            console.log(response);
            this.access_token = response.access_token
            this.user = response.user
            localStorage.setItem(KEY_USER, JSON.stringify({ access_token: response.access_token, user: response.user }))
            this.status = "done"
        } catch (err) {
            console.log({ err });
            this.status = "error"
            this.errorMessage = err
        }
    }

    init() {
        let response = localStorage.getItem(KEY_USER)
        if (response) {
            response = JSON.parse(response)
            this.access_token = response.access_token
            this.user = response.user
        }

    }
}
const userState = new UserStore()