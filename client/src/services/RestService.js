
export class RestService {

    
    API_URL = "http://192.168.1.108:5000/api"

    getAuthorizationHeader = (access_token) => {
        return {
            "Content-type": "application/json",
            Authorization: `Bearer ${access_token}`
        }
    }

    getHeader = () => {
        return {
            "Content-type": "application/json",
        }
    }

    get = async (url, addHeaders) => {
        const headers = this.getAuthorizationHeader(addHeaders?.access_token)
        return fetch(this.API_URL + url, {
            headers
        })
    }

    post = async (url, body, addHeaders) => {
        const headers = this.getAuthorizationHeader(addHeaders?.access_token)
        return fetch(this.API_URL + url, {
            method: "POST",
            headers,
            body
        })
    }
}

export const restService = new RestService()