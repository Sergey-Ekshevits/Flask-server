import React from 'react';
import { ResponsiveAppBar } from './components/AppBar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { HomePage } from "./pages/HomePage"
import { useStore } from './store/context';
import { LoginPage } from './pages/LoginPage';
import { RegisterPage } from './pages/RegisterPage';
import { observer } from "mobx-react"
export const MainRoutes = observer(() => {
    const user = useStore((state) => state.userStore.user)
    const logout = useStore((state) => state.userStore.logout)
    
    return (
        <BrowserRouter>
            <ResponsiveAppBar user={user} logout={logout} />
            <Routes>
                <Route path="/"  element={<HomePage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/registrate" element={<RegisterPage />} />
            </Routes>
            
        </BrowserRouter>
    )
})