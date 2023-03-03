import { userStore } from "../store/User"

class RestService {


    getHeader = () => {
        return {
            "Content-type": "application/json",
            access_token: userStore.access_token,
            Authorization: `Bearer ${userStore.access_token}`
        }
    }

    post = async (url) => {
        const headers = this.getHeader()
        console.log(headers);
        return fetch(url, {
            headers
        })
    }
}

export const restService = new RestService();