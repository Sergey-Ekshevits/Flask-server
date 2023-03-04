
export class RestService {


    API_URL = "http://192.168.1.108:5000/api"
    userStore = null;
    constructor(userStore) {
        this.userStore = userStore
    }
    getAuthorizationHeader = () => {
        return {
            "Content-type": "application/json",
            Authorization: `Bearer ${this.userStore.access_token}`
        }
    }

    getHeader = () => {
        return {
            "Content-type": "application/json",
        }
    }

    fetch = async (endpoint, data, attempt = 5) => {
        const url = this.API_URL + endpoint
        return fetch(url, data).then((response) => {
            if (attempt <= 0) {
                this.userStore.logout()
                return
            }
            if (response.status === 422 && attempt > 0) {
                return this.fetch(endpoint, data, --attempt)
            }
            return response;
        })
    }

    get = async (url) => {
        const headers = this.getAuthorizationHeader()
        return this.fetch(url, {
            headers
        })
    }

    post = async (url, body) => {
        const headers = this.getAuthorizationHeader()
        return this.fetch(url, {
            method: "POST",
            headers,
            body
        })
    }
}

