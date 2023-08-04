import React from "react";
import { useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import useUser from "../hooks/useUser";
import { Token } from "../interfaces/token";
import { User } from "../interfaces/user";
import axios from "../axios";
import { Transaction } from "../interfaces/Transactions";
import useAxiosPrivate from "../hooks/useAxiosPrivate";

const Transactions: React.FC = () => {
    const userContextValue = useUser();
    const axiosPrivate = useAxiosPrivate();
    const navigate = useNavigate();
    const user = userContextValue?.user;
    const authContextValue = useAuth();
    const auth = authContextValue?.auth;
    const setUser = userContextValue?.setUser;
    const [transactions, setTransactions] = React.useState<Transaction[]>();

    const getUserInfo = async (token: Token) => {
        try {
            const response = await axios.get("/auth/users/me/", {
                headers: {
                    Authorization: `Bearer ${token.access_token}`,
                },
            });
            let user: User = response.data;
            setUser?.(user);
            navigate("/home");
        } catch (error) {
            console.log(error);
        }
    };

    React.useEffect(() => {
        if (auth) {
            getUserInfo(auth);
        }
    }, [auth]);

    const getTransactions = async (user_id: number) => {
        let isMounted = true;
        const controller = new AbortController();
        try {
            const response = await axiosPrivate.get(`/tran/transaction/user/${user_id}`, {
                signal: controller.signal,
            });

            if (isMounted) {
                const transactions: Transaction[] = response.data;
                setTransactions(transactions);
            }
        } catch (error) {
            console.log(error);
        }
    };

    React.useEffect(() => {
        if (userContextValue?.user) {
            getTransactions(userContextValue.user.user_id);
        }, [userContextValue?.user]);


    return (
        <div>
            
        </div>
    );
}
