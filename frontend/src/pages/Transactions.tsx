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



    React.useEffect(() => {
        const fetchTransactions = async () => {
          if (user?.user_id) {
            const controller = new AbortController();
            try {
              const transactionResponse = await axiosPrivate.get(`/tran/transaction/user/${user.user_id}`, {
                signal: controller.signal,
              });
      
              const transactions: Object = transactionResponse.data;
      
              const updatedReturned: { [key: string]: boolean } = {};
              Object.entries(transactions).forEach(([transaction_id, media_titles]) => {
                media_titles.forEach((title: string) => {
                  const key = `${transaction_id} ${title}`;
                  updatedReturned[key] = false;
                });
              });
      
              const returnedResponse = await axiosPrivate.get(`/ret/returned/${user.user_id}`, {
                signal: controller.signal,
              });
      
              const returnedData: Object = returnedResponse.data;
              Object.entries(returnedData).forEach(([key, bool]) => {
                updatedReturned[key] = true;
              });
      
              setTransactions(transactions);
              setReturned(updatedReturned);
            } catch (error) {
              console.log(error);
            }
          }
        };
      
        fetchTransactions();
      }, [user?.user_id]);

    


    const handleReturn = async (mediaTitle: string, transaction_id: string) => {
        const id: number = +transaction_id;
        const data = {
            transaction_id: id,
            title: mediaTitle
        }
        let isMounted = true;
        const controller = new AbortController();
        try {
            const response = await axiosPrivate.put(`/inv/inventory/return/${mediaTitle}`, {
                signal: controller.signal,
            });

            const response2 = await axiosPrivate.post(`/ret/returned/`, data, {
                signal: controller.signal,
            });

            if (isMounted) {
                const updatedReturned = { ...returned };
                updatedReturned[`${transaction_id} ${mediaTitle}`] = true;
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
                                                                onClick={() => returned[`${transaction_id} ${title}`] ? null : handleReturn(title, transaction_id)}
                                                                style={{ backgroundColor: returned[`${transaction_id} ${title}`] ? 'lightgreen' : 'lightcoral' }}
                                                            >
                                                                {returned[`${transaction_id} ${title}`] ? 'Returned' : 'Return?'}
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
