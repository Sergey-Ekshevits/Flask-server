import './App.css';
import { useEffect, useState } from 'react';
import { PostList } from "./components/PostList"
import { RegistrateForm } from "./components/RegistrateForm"
import { LoginForm } from "./components/LoginForm"
import { MainRoutes } from "./pages/Routes"
import { observer } from "mobx-react"
import { StoreProvider } from "./store/context"
import { store } from "./store/root"

const App = observer(() => {
  return (
    <StoreProvider store={store}>
      <MainRoutes />
      {/* <div className="App">
        <header className="App-header">
          <PostList />
          <RegistrateForm />
          <LoginForm />
        </header>
      </div> */}
    </StoreProvider>
  );
})

export default App;
