import './App.css';
import { useEffect, useState } from 'react';
import { PostList } from "./components/PostList"
import { RegistrateForm } from "./components/RegistrateForm"
import { LoginForm } from "./components/LoginForm"
import { MainRoutes } from "./pages/Routes"
import { observer } from "mobx-react"
import { StoreProvider } from "./store/context"
import { store } from "./store/root"
import EventEmitter from 'events';
import { AppProvider } from "./contexts/AppContext"

const eventEmitter = new EventEmitter();
const App = observer(() => {
  return (
    <StoreProvider store={store}>
      <AppProvider value={{ eventEmitter }}>
        <MainRoutes />
        {/* <div className="App">
        <header className="App-header">
          <PostList />
          <RegistrateForm />
          <LoginForm />
        </header>
      </div> */}
      </AppProvider>
    </StoreProvider>
  );
})

export default App;
