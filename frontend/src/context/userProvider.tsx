import React, { useState, createContext } from "react";
import { User, Employee } from "../interfaces/user";

interface UserContextType {
    user: User | Employee | null;
    setUser: React.Dispatch<React.SetStateAction<User | Employee | null>>;
}

const UserContext = createContext<UserContextType | null>(null);

export const UserProvider: React.FunctionComponent<React.PropsWithChildren<{value: User| Employee | null}>> = ({ value, children }) => {
    const [user, setUser] = useState<User | Employee | null>(value);


    const userContextValue: UserContextType = {
        user,
        setUser,
    };

    return (
        <UserContext.Provider value={userContextValue}>
            {children}
        </UserContext.Provider>
    );
};


export default UserContext;