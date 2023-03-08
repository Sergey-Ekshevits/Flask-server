import { API_URL } from "../constant"

export class RestService {


    API_URL = API_URL
    userStore = null;

    constructor(userStore) {
        this.userStore = userStore
    }

    getAuthorizationHeader = (refresh) => {
        const token = refresh ? this.userStore.refresh_token : this.userStore.access_token
        return {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        }
    }

    getHeader = () => {
        return {
            "Content-Type": "application/json",
        }
    }

    getFormDataHeader = () => {
        return {
            // "Content-type": "application/x-www-form-urlencoded",
            "Content-Type": "multipart/form-data",
        }
    }

    fetch = async (endpoint, data = {}, additionalHeader = {}, attempt = 2) => {
        const url = this.API_URL + endpoint
        let headers = this.getAuthorizationHeader()
        headers = { ...headers, ...additionalHeader }
        return fetch(url, { ...data, headers }).then(async (response) => {
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

    patchWithAttempt = async (url, body, additionalHeader) => {
        return this.fetch(url, {
            method: "PATCH",
            body,
        }, additionalHeader
        )
    }

    patchMultiData = async (url, body) => {
        const headers = this.getAuthorizationHeader()
        delete headers['Content-Type']
        return fetch(this.API_URL + url, {
            method: "PATCH",
            body,
            headers
        })
    }

    postWithAttempt = async (url, body, additionalHeader) => {
        return this.fetch(url, {
            method: "POST",
            body
        }, additionalHeader)
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

