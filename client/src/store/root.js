import { makeAutoObservable } from "mobx";
import { UserStore } from "./User";
import { PostStore } from "./Post";

class RootStore {
    userStore = new UserStore();
    postStore = new PostStore(this.userStore);

    constructor() {
        makeAutoObservable(this);
    }
}

export const store = new RootStore();
