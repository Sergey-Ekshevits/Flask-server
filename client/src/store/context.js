import React from "react"
import { createContext, useContext } from "react";
import { RootStore } from "./root"

const StoreContext = createContext(null);


export function StoreProvider(props) {
  return (
    <StoreContext.Provider value={props.store}>
      {props.children}
    </StoreContext.Provider>
  );
}


export function useStore(selector) {
  const store = useContext(StoreContext);

  if (!store) {
    throw new Error("Can not `useStore` outside of the `StoreProvider`");
  }

  if (typeof selector === "function") {
    return selector(store);
  }

  return store;
}
