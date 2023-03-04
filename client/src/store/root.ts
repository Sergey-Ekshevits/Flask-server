import { makeAutoObservable } from "mobx";
import { UserStore } from "./User";
import { PostStore } from "./Post";
import { RestService } from "../services/RestService";

class RootStore {
    userStore = new UserStore();
    postStore = new PostStore();
    
    constructor() {
        makeAutoObservable(this);
    }
}
export type { RootStore };
export const store = new RootStore();

