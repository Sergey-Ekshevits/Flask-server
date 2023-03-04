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
            const posts = await restService.get("/posts").then((res) => res.json()).catch(() => [])
            console.log({ posts });
            this.posts = posts
            this.status = "done"
        } catch (err) {
            this.status = "error"
            this.errorMessage = err
        }
    }
}
