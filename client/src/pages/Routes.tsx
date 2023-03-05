import React from 'react';
import { ResponsiveAppBar } from '../components/AppBar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { HomePage } from "./HomePage"
import { useStore } from '../store/context';
import { LoginPage } from './LoginPage';
import { RegisterPage } from './RegisterPage';
import { observer } from "mobx-react"
import { PostPage } from './PostPage';
import { ProtectedRoute } from '../components/ProtectedRoute';
import { ProfilePage } from './ProfilePage';
export const MainRoutes = observer(() => {
    const user = useStore((state) => state.userStore.user)
    const logout = useStore((state) => state.userStore.logout)

    return (
        <BrowserRouter>
            <ResponsiveAppBar user={user} logout={logout} />
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/registrate" element={<RegisterPage />} />
                <Route path="/profile" element={<ProfilePage />} />
                <Route path="/post/:id"
                    element={
                        <ProtectedRoute user={user}>
                            <PostPage />
                        </ProtectedRoute>
                    } />
            </Routes>

        </BrowserRouter>
    )
})