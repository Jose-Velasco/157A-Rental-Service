import React, { useState, createContext } from "react";
import { Token } from "../interfaces/token";

// Define the context type
interface AuthContextType {
    auth: Token | null;
    setAuth: React.Dispatch<React.SetStateAction<Token | null>>;
}

const AuthContext = createContext<AuthContextType | null>(null);

export const AuthProvider: React.FunctionComponent<React.PropsWithChildren<{
    initialAccessToken: Token | null;
}>> = ({ initialAccessToken, children }) => {
    const [auth, setAuth] = useState<Token | null>(initialAccessToken);

    const authContextValue: AuthContextType = {
        auth,
        setAuth,
    };

    return (
        <AuthContext.Provider value={ authContextValue }>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthContext;