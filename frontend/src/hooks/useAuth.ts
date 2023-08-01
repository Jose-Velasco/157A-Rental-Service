import { useContext, useDebugValue } from "react";
import AuthContext from "../context/authProvider";

const useAuth = () => {
    const contextValue = useContext(AuthContext);
    const auth = contextValue?.auth;
    useDebugValue(auth, auth => auth?.access_token ? "Logged in" : "Logged out");
    return contextValue;
}

export default useAuth;