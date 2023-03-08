import {API_URL} from "../constant"

export class RestService {


    API_URL = API_URL
    userStore = null;

    constructor(userStore) {
        this.userStore = userStore
    }

    getAuthorizationHeader = (refresh, isForm) => {
        const contentType = isForm ? "application/x-www-form-urlencoded" : "application/json";
        const token = refresh ? this.userStore.refresh_token : this.userStore.access_token
        return {
            "Content-type": contentType,
            Authorization: `Bearer ${token}`
        }
    }

    getHeader = () => {
        return {
            "Content-type": "application/json",
        }
    }

    fetch = async (endpoint, data = {}, isForm = false, attempt = 2) => {
        const url = this.API_URL + endpoint
        const headers = this.getAuthorizationHeader(false, true)
        return fetch(url, {...data, headers}).then(async (response) => {
            if (attempt < 0) {
                this.userStore.logout()
                return
            }
            if (response.status === 401) {
                await this.userStore.refreshToken()
                return this.fetch(endpoint, data, --attempt)
            }
            return response;
        })
    }

    getWithAttempt = async (url) => {
        return this.fetch(url)
    }

    patchWithAttempt = async (url, body, isForm) => {
        return this.fetch(url, {
            method: "PATCH",
            body
        }, isForm)
    }

    postWithAttempt = async (url, body) => {
        return this.fetch(url, {
            method: "POST",
            body
        })
    }

    deleteWithAttempt = async (url) => {
        return this.fetch(url, {
            method: "DELETE"
        })
    }

    post = async (url, body, refresh) => {
        const headers = this.getAuthorizationHeader(refresh)
        return fetch(this.API_URL + url, {
            method: "POST",
            headers,
            body
        })
    }

    get = async (url) => {
        const headers = this.getAuthorizationHeader()
        return fetch(this.API_URL + url, {
            headers
        })
    }
}

