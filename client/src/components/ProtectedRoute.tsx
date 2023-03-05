import { Navigate } from "react-router-dom";
import { ReactNode } from "react"
type Props = {
    user: any;
    children?: ReactNode
}
export const ProtectedRoute = ({ user, children }: Props) => {
    if (!user) {
        return <Navigate to="/login" replace={true} />;
    }

    return <>{children}</>;
};