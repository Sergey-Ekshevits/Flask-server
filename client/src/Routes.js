import { ResponsiveAppBar } from './components/AppBar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { HomePage } from "./pages/HomePage"
export const MainRoutes = () => {

    return (
        <Router>
            <ResponsiveAppBar/>
            <Routes>
                <Route path="/" element={<HomePage />} />
            </Routes>
        </Router>
    )
}