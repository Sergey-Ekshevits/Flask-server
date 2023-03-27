import { makeAutoObservable } from "mobx"
import { restService } from "./context"
import {LocalStorageDto, UserDto} from "../types";

const KEY_USER = "KEY_USER"


export class UserStore {
    user: null | UserDto = null
    access_token: null | string = null
    refresh_token: null | string = null
    status = ""
    errorMessage = ""

    constructor() {
        makeAutoObservable(this)
        this.init();
    }

    registrate = async (name: string,
        email: string,
        password: string,
        repeatPassword: string) => {
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
            this.errorMessage = err as string
        }
    }

    login = async (email: string, password: string) => {
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
            this.errorMessage = err as string
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
            this.errorMessage = err as string
        }
    }

    init() {
        let response = localStorage.getItem(KEY_USER)
        if (response) {
            const data: LocalStorageDto = JSON.parse(response)
            if (data) {
                this.access_token = data.access_token
                this.refresh_token = data.refresh_token
                this.user = data.user
            }

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


    updateCurrentUser = async (name: string, email: string, file: File | null) => {
        if (this.status === "loading") {
            return
        }
        this.status = "loading"
        const formData = new FormData();
        formData.append('name', name)
        formData.append('email', email)
        if (file) {
            formData.append('file', file)
        }
        const response = await restService.postWithAttempt("/update_user", formData);
        const json = await response.json();
        if (response.status === 200) {
            this.access_token = json.access_token
            
            this.status = "success"
        } else {
            this.status = "done"
            this.errorMessage = json.msg
        }
    }
}
// const userState = new UserStore()