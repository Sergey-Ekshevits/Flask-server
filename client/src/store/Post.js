import {makeAutoObservable} from "mobx"
import {restService} from "./context"

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
            const posts = await restService.getWithAttempt("/posts")
                .then((res) => res.json()).catch(() => [])
            console.log({posts});
            this.posts = posts
            this.status = "done"
        } catch (err) {
            this.status = "error"
            this.errorMessage = err
        }
    }

    getPost = async (id) => {
        if (this.status === "loading") {
            return
        }
        try {
            this.status = "loading"
            const post = await restService.postWithAttempt("/post/" + id)
                .then((res) => res.json()).catch(() => {})
            //     console.log({posts});
            // const post = this.posts.find((p) => Number(id) === p.id)
            this.status = "done"
            return post;
        } catch (err) {
            this.status = "error"
            this.errorMessage = err
        }
    }


    updatePost = async (id, title, body, image) => {
        if (this.status === "loading") {
            return
        }
        try {
            const data = new FormData()
            data.append("title", title.trim())
            data.append("body", body.trim())
            if (image) {
                data.append("file", image)
            }
            this.status = "loading"
            const response = await restService.patchMultiData(`/post/${id}`,
                data,
            )
            console.log({response});
            if (response.status === 200) {
                this.status = "success"
                const json = await response.json();
                return json.post;
            } else {

                this.status = "done"
            }
            // this.posts = posts
        } catch (err) {
            this.status = "error"
            this.errorMessage = err
        }
    }

    deletePost = async (id) => {
        try {
            console.log({id})
            // await new Promise((res) => setTimeout(res, 3000))
            const response = await restService.deleteWithAttempt(`/post/${id}`)
            // const response = {}
            console.log({response});
            if (response.status === 200) {
                this.status = "success"

            } else {
                this.status = "done"
            }
        } catch (err) {
            this.status = "error"
            this.errorMessage = err
        }
    }
}
