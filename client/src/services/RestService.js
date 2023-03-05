import { API_URL } from "../constant"

export class RestService {


    API_URL = API_URL
    userStore = null;
    constructor(userStore) {
        this.userStore = userStore
    }
    getAuthorizationHeader = (refresh) => {
        const token = refresh ?  this.userStore.refresh_token : this.userStore.access_token

        console.log( `Authorization: Bearer ${token}`);
        return {
            "Content-type": "application/json",
            Authorization: `Bearer ${token}`
        }
    }

    getHeader = () => {
        return {
            "Content-type": "application/json",
        }
    }

    fetch = async (endpoint, data = {}, attempt = 1) => {
        const url = this.API_URL + endpoint
        const headers = this.getAuthorizationHeader()
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

    postWithAttempt = async (url, body) => {
        return this.fetch(url, {
            method: "POST",
            body
        })
    }

    post = async (url, body, refresh) => {
        const headers = this.getAuthorizationHeader(refresh)
        console.log({refresh});
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

