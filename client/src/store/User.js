import { makeAutoObservable } from "mobx"
import { restService } from "./context"

const KEY_USER = "KEY_USER"
export class UserStore {
    user = null
    access_token = null
    refresh_token = null
    status = ""
    errorMessage = ""

    constructor() {
        makeAutoObservable(this)
        this.init();
    }

    registrate = async (name,
        email,
        password,
        repeatPassword) => {
        if (this.status === "loading") {
            return
        }
        try {
            this.status = "loading"
            const response = await restService.post("/registrate", JSON.stringify({
                name,
                email,
                password,
                repeatPassword,
            }))
            const json = await response.json();
            if (response.status === 200) {
                console.log();
                this.access_token = json.access_token
                this.refresh_token = json.refresh_token
                this.user = json.user
                localStorage.setItem(KEY_USER, JSON.stringify({
                    access_token: json.access_token,
                    refresh_token: json.refresh_token,
                    user: json.user
                }))
                this.status = "success"
            } else {
                this.status = "done"
                this.errorMessage = json.msg
            }
        } catch (err) {
            console.log({ err });
            this.status = "error"
            this.errorMessage = err
        }
    }

    login = async (email, password) => {
        if (this.status === "loading") {
            return
        }
        try {
            this.status = "loading"
            const response = await restService.post("/login", JSON.stringify({
                email,
                password,
            }));
            const json = await response.json();
            if (response.status === 200) {
                console.log();
                this.access_token = json.access_token
                this.refresh_token = json.refresh_token
                this.user = json.user
                localStorage.setItem(KEY_USER, JSON.stringify({
                    access_token: json.access_token,
                    refresh_token: json.refresh_token,
                    user: json.user
                }))
                this.status = "success"
            } else {
                this.status = "done"
                this.errorMessage = json.msg
            }
        } catch (err) {
            console.log({ err });
            this.status = "error"
            this.errorMessage = err
            return Promise.reject();
        }
    }

    logout = async () => {
        try {
            this.status = "loading"
            // const response = await restService.post("/logout", JSON.stringify({
            //     email,
            //     password,
            // })).then((res) => res.json())
            // console.log(response);
            this.access_token = null
            this.user = null
            localStorage.removeItem(KEY_USER)
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
            this.refresh_token = response.refresh_token
            this.user = response.user
        }

    }

    refreshToken = async () => {
        const response = await restService.post("/refresh", "", true);
        const json = await response.json();
        if (response.status === 200) {
            this.access_token = json.access_token
            localStorage.setItem(KEY_USER, JSON.stringify({
                access_token: json.access_token,
                refresh_token: this.refresh_token,
                user: this.user
            }))
            this.status = "success"
        } else {
            this.status = "done"
            this.errorMessage = json.msg
        }
    }
}
// const userState = new UserStore()