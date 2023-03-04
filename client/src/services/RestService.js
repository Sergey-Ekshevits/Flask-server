import { userStore } from "../store/User"

class RestService {

    API_URL = "http://192.168.1.34:5000/api"
    getAuthorizationHeader = () => {
        return {
            "Content-type": "application/json",
            Authorization: `Bearer ${userStore.access_token}`
        }
    }

    getHeader = () => {
        return {
            "Content-type": "application/json",
        }
    }

    get = async (url, headers = this.getHeader()) => {
        // const headers = this.getAuthorizationHeader()
        return fetch(this.API_URL + url, {
            headers
        })
    }

    post = async (url, body, headers = this.getHeader()) => {
        // const headers = this.getAuthorizationHeader()
        return fetch(this.API_URL + url, {
            method: "POST",
            headers,
            body
        })
    }
}

export const restService = new RestService();