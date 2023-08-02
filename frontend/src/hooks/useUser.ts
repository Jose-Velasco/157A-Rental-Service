import { useContext, useDebugValue } from "react";
import UserContext  from "../context/userProvider";

const useUser = () => {
    const contextValue = useContext(UserContext);
    const user = contextValue?.user;
    useDebugValue(user, user => user?.first_name ? "Logged in" : "Logged out");
    return contextValue;
};

export default useUser;