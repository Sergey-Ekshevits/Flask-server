import { makeAutoObservable } from "mobx"
import { restService } from "../services/RestService"

export class PostStore {
    posts = []
    status = null
    errorMessage = null
    userStore = null
    constructor(userStore) {
        makeAutoObservable(this)
        this.userStore = userStore;
    }

    getPosts = async () => {
        const access_token = this.userStore.access_token
        try {
            this.status = "loading"
            const posts = await restService.get("/posts", { access_token }).then((res) => res.json()).catch(() => [])
            this.posts = posts
            this.status = "done"
        } catch (err) {
            this.status = "error"
            this.errorMessage = err
        }
    }
}
