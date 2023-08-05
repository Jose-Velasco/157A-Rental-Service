import React from "react";
import { useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import useUser from "../hooks/useUser";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import ReusableBar from "../components/ReusableBar";
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';

const Transactions: React.FC = () => {
    const userContextValue = useUser();
    const axiosPrivate = useAxiosPrivate();
    const navigate = useNavigate();
    const user = userContextValue?.user;
    const authContextValue = useAuth();
    const auth = authContextValue?.auth;
    const setUser = userContextValue?.setUser;
    const [transactions, setTransactions] = React.useState<Object>([]);
    const [returned, setReturned] = React.useState<{ [key: string]: boolean }>({});

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

    React.useEffect(() => {
        if (transactions) {

            const updatedReturned: { [key: string]: boolean } = {};
            Object.entries(transactions).forEach(([transaction_id, media_titles]) => {
                // Initialize each media_titles array with false values
                media_titles.forEach((title: string) => {
                    updatedReturned[title] = false;
                });
            });
            setReturned(updatedReturned);
            console.log(returned);
        }
    }, []);


    const handleReturn = async (mediaTitle: string) => {
        let isMounted = true;
        const controller = new AbortController();
        try {
            const response = await axiosPrivate.put(`/inv/inventory/return/${mediaTitle}`, {
                signal: controller.signal,
            });

            if (isMounted) {
                const updatedReturned = { ...returned };
                updatedReturned[mediaTitle] = true;
                setReturned(updatedReturned);
            }
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <>
            <ReusableBar title="Transactions" />

            <div style={{ marginTop: '100px' }}>
                <h1 style={{ fontFamily: "Trebuchet MS, sans-serif" }}>Transactions</h1>
                {Object.entries(transactions || {}).map(([transaction_id, media_titles]) => (
                    //space tables apart
                    <React.Fragment key={transaction_id}>
                        <Box sx={{ bgcolor: '#757DE8', height: '1vh' }} />
                        <TableContainer component={Paper}>
                            <Table sx={{ minWidth: 700 }} aria-label="customized table">
                                <TableHead>
                                    <TableRow>
                                        <TableCell align="center" style={{ background: "lightblue", fontSize: "large" }}>Transaction {transaction_id}</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {media_titles.map((title: string) => (

                                        <TableRow
                                            key={title}
                                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                        >
                                            <div style={{ display: "flex", alignItems: "center", justifyContent: "center" }}>
                                                <TableCell component="th" scope="row" align="center">
                                                    <ul style={{
                                                        listStyleType: "none",
                                                        padding: 0,
                                                        margin: 0,
                                                        display: "flex",
                                                        justifyContent: "center",
                                                        alignItems: "center"
                                                    }}>
                                                        <li style={{
                                                            marginRight: "20px"
                                                        }}>{title}</li>

                                                        <li>

                                                            <Button
                                                                variant="outlined"
                                                                onClick={() => handleReturn(title)}
                                                                style={{ backgroundColor: returned[title] ? 'lightgreen' : 'lightcoral' }}
                                                            >
                                                                {returned[title] ? 'Returned' : 'Return?'}
                                                            </Button>
                                                        </li>
                                                    </ul>

                                                </TableCell>
                                            </div>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </TableContainer>
                    </React.Fragment>
                ))}
            </div>
        </>
    )
};

export default Transactions;
