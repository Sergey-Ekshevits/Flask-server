import React from "react"
import { createContext, useContext } from "react";
import { RestService } from "../services/RestService";
import { RootStore, store } from "./root"
export const restService = new RestService(store.userStore);
const StoreContext = createContext<RootStore | null>(null);
interface StoreProviderProps {
  store: RootStore;
  children: React.ReactNode;
}


export function StoreProvider(props: StoreProviderProps) {
  return (
    <StoreContext.Provider value={props.store}>
      {props.children}
    </StoreContext.Provider>
  );
}


export function useStore(): RootStore;
export function useStore<Result>(
  selector: (value: RootStore) => Result
): Result;
export function useStore<Result>(selector?: (value: RootStore) => Result) {
  const store = useContext(StoreContext);

  if (!store) {
    throw new Error("Can not `useStore` outside of the `StoreProvider`");
  }

  if (typeof selector === "function") {
    return selector(store);
  }

  return store;
}
