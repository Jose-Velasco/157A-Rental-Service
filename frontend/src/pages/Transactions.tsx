import React from "react";
import { useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import useUser from "../hooks/useUser";
import { Token } from "../interfaces/token";
import { User } from "../interfaces/user";
import axios from "../axios";
import { Transaction } from "../interfaces/Transactions";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { MediaMixed } from "../interfaces/MediaInterfaces";
import { Rented } from "../interfaces/Rented";
import { MediaContent } from "../interfaces/MediaContentInterface";
import ReusableBar from "../components/ReusableBar";
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';

const Transactions: React.FC = () => {
    const userContextValue = useUser();
    const axiosPrivate = useAxiosPrivate();
    const navigate = useNavigate();
    const user = userContextValue?.user;
    const authContextValue = useAuth();
    const auth = authContextValue?.auth;
    const setUser = userContextValue?.setUser;
    const [transactions, setTransactions] = React.useState<Object>([]);


    const getTransactions = async (user_id: number) => {
        let isMounted = true;
        const controller = new AbortController();
        try {
            const response = await axiosPrivate.get(`/tran/transaction/user/${user_id}`, {
                signal: controller.signal,
            });

            if (isMounted) {
                const transactions: Object = response.data;
                setTransactions(transactions);
            }
        } catch (error) {
            console.log(error);
        }
    };

    React.useEffect(() => {
       if (user?.user_id) {
              getTransactions(user.user_id);
         }
    }, []);

   
    

    

    return (
        <>
            <ReusableBar title = "Transactions"/>
            <div style = {{marginTop: '100px'}}>
            <h1 style = {{fontFamily: "Trebuchet MS, sans-serif"}}>Transactions</h1>
            {Object.entries(transactions || {}).map(([transaction_id, media_titles]) => (
                //space tables apart
                <>
                    <Box sx={{ bgcolor: '#757DE8', height: '1vh' }} /><TableContainer component={Paper}>
                        <Table sx={{ minWidth: 700}} aria-label="customized table">
                            <TableHead>
                                <TableRow>
                                    <TableCell align = "center" style = {{background: "lightblue", fontSize: "large"}}>Transaction {transaction_id}</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {media_titles.map((title: string) => (
                                    <TableRow
                                        key={title}
                                        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                    >
                                        <TableCell component="th" scope="row" align="center">
                                            {title}
                                        </TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer></>
            
            ))}
            </div>
        </>
    );
}

export default Transactions;
