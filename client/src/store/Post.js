import { makeAutoObservable } from "mobx"
import { restService } from "./context"

export class PostStore {
    posts = []
    status = null
    errorMessage = null
    constructor() {
        makeAutoObservable(this)
    }

    getPosts = async () => {
        if (this.status === "loading") {
            return
        }
        try {
            this.status = "loading"
            const posts = await restService.getWithAttempt("/posts").then((res) => res.json()).catch(() => [])
            this.posts = posts
            this.status = "done"
        } catch (err) {
            this.status = "error"
            this.errorMessage = err
        }
    }
}
