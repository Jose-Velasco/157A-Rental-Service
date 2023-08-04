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

const Transactions: React.FC = () => {
    const userContextValue = useUser();
    const axiosPrivate = useAxiosPrivate();
    const navigate = useNavigate();
    const user = userContextValue?.user;
    const authContextValue = useAuth();
    const auth = authContextValue?.auth;
    const setUser = userContextValue?.setUser;
    const [transactions, setTransactions] = React.useState<Transaction[]>([]);
    const [media, setMedia] = React.useState<MediaContent[]>([]);
    const [rentedMedia, setRentedMedia] = React.useState<Rented[]>([]);
    const [mediaTitle, setMediaTitle] = React.useState<string[]>([]);


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

    const getMediaMixed = async (media_id: number) => {
        let isMounted = true;
        const controller = new AbortController();
        try {
            const response = await axiosPrivate.get(`/media/details/${media_id}`, {
                signal: controller.signal,
            });

            if (isMounted) {
                const media: MediaContent = response.data;
                //insert into MediaContent array
                setMedia((prevMedia) => [...prevMedia, media]);
            }
        } catch (error) {
            console.log(error);
        }
    }

    const getMediaIDs = async (transaction_id: number) => {
        let isMounted = true;
        const controller = new AbortController();
        try {
            const response = await axiosPrivate.get(`/rent/rented/${transaction_id}`, {
                signal: controller.signal,
            });

            if (isMounted) {
                const rented:Rented[] = response.data;
                setRentedMedia(rented);
            }
        } catch (error) {
            console.log(error);
        }
    }

    React.useEffect(() => {
        const fetchTransactionsAndRelatedData = async () => {
            try {
                const user_id = user?.user_id ?? -1;
                const response = await axiosPrivate.get(`/tran/transaction/user/${user_id}`);
                const transactions: Transaction[] = response.data;
                setTransactions(transactions);
    
                const rentedMediaPromises = transactions.map(async (transaction) => {
                    const rentedResponse = await axiosPrivate.get(`/rent/rented/${transaction.transaction_id}`);
                    return rentedResponse.data;
                });
                const rentedMediaResults = await Promise.all(rentedMediaPromises);
                setRentedMedia(rentedMediaResults.flat());
    
                const mediaPromises = rentedMediaResults.flat().map(async (rented) => {
                    const mediaResponse = await axiosPrivate.get(`/media/details/${rented.media_id}`);
                    return mediaResponse.data;
                });
                const mediaResults = await Promise.all(mediaPromises);
                setMedia(mediaResults);
                console.log(media)
            } catch (error) {
                console.log(error);
            }
        };
        
        fetchTransactionsAndRelatedData();
    }, [user, axiosPrivate]);

    React.useEffect(() => {
        // Check if media is not empty
        if (media.length > 0) {
            // Map the media to titles and update the mediaTitle state
            const mediaTitles = media.map((mediaItem) => {
                setMediaTitle((prevMedia) => [...prevMedia, mediaItem.title]);
            }
            );
        }
    }, [media]);
    

    

    return (
        <>
            <ReusableBar title = "Transactions"/>
            <h1>Transactions</h1>
            <ul>
                {rentedMedia?.map((rented) => (
                    <li key={rented.transaction_id}>
                        <p>Transaction ID: {rented.transaction_id}</p>
                        <p>Rent Duration: {rented.media_id}</p>
                    </li>
                ))}
            </ul>
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 700 }} aria-label="customized table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Transacted Media</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {mediaTitle?.map((title) => (
                            <TableRow
                                key={title}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            >
                                <TableCell component="th" scope="row">
                                    {title}
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    );
}

export default Transactions;
