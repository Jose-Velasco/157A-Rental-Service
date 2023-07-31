import React, { useEffect } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import {Link} from "react-router-dom";
import axios from "../axios";


const EmployeeSignIn:React.FC = () => {

    const [users, setUsers] = useState();
    
    useEffect(() => {
        let isMounted = true;
        const controller = new AbortController();

        const getUsers = async () => {
            try{
                const response = await axios.get("/users",{
                    signal: controller.signal,
                });
                console.log(response.data)
                if(isMounted){
                    setUsers(response.data);
                }
            }catch(error){
                console.log(error);
            }
        }
        getUsers();
        //Cleanup
        return() => {
            isMounted = false;
            controller.abort();
        }

    },[]);

    return(
        <form>
    <Typography align="center" gutterBottom fontSize={35}> Employee Sign In</Typography>
            <TextField label = "Email" type = "email" fullWidth/>
            <TextField label = "Password*" type = "password" fullWidth/>
            <Link to = "/employeehome" style = {{textDecoration: 'none'}}>
            <Button type = "submit" fullWidth variant = "contained" color = "primary" sx={{mt:3,mb:2}}>Sign In</Button>
            </Link>
            <Link to = "/" style = {{textDecoration: 'none'}}>
            <Button type = "submit" fullWidth variant = "contained" color = "success" sx={{mt:3,mb:2}}>Return to Customer Sign In</Button>
            </Link>
        </form>
    );
};


export default EmployeeSignIn;