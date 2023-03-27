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

    fetchAttempts = async (endpoint, data = {}, additionalHeader = {}, attempt = 2) => {
        const url = this.API_URL + endpoint
        const headers = { ...this.getAuthorizationHeader(), ...additionalHeader }
        const options = { ...data, headers };
        return fetch(url, options).then(async (response) => {
            if (attempt < 0) {
                this.userStore.logout()
                return
            }
            if (response.status === 422) {
                this.userStore.logout()
                return
            }
            if (response.status === 401) {
                try {
                    await this.userStore.refreshToken()
                } catch (error) {
                    console.log({error});
                    return;
                }
                return this.fetchAttempts(endpoint, data, additionalHeader, --attempt)
            }
            return response;
        }).catch((error) => {
            console.log({ error });
        })
    }

    getWithAttempt = async (url) => {
        const additionalHeader = this.getHeader()
        return this.fetchAttempts(url, {}, additionalHeader)
    }

    patchWithAttempt = async (url, body) => {
        const additionalHeader = this.getHeader()
        return this.fetchAttempts(url,
            {
                method: "PATCH",
                body,
            },
            additionalHeader
        )
    }

    patchMultiData = async (url, body) => {
        return this.fetchAttempts(url,
            {
                method: "PATCH",
                body,
            },
        )
    }

    postWithAttempt = async (url, body) => {
        const additionalHeader = this.getHeader()
        return this.fetchAttempts(url,
            {
                method: "POST",
                body
            },
            additionalHeader)
    }

    deleteWithAttempt = async (url) => {
        return this.fetchAttempts(url, {
            method: "DELETE"
        })
    }

    post = async (url, body, refresh) => {
        const headers = {
            ...this.getAuthorizationHeader(refresh),
            ...this.getHeader(),
        }
        return fetch(this.API_URL + url, {
            method: "POST",
            headers,
            body
        })
    }

    get = async (url) => {
        const headers = {
            ...this.getAuthorizationHeader(),
            ...this.getHeader(),
        }
        return fetch(this.API_URL + url, {
            headers
        })
    }
}

