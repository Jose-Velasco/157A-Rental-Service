import React, { useEffect, useCallback } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import {Link} from "react-router-dom";
import axios from "../axios";
import useAuth from "../hooks/useAuth";
import { Token } from "../interfaces/token";


const LOGIN_URL = "/auth/token/";

const LoginForm:React.FC = () => {
    const [users, setUsers] = useState();
    const [formData, setFormData] = useState({
        username: "",
        password: "",
    });
    const authContextValue = useAuth();
    const setAuth = authContextValue?.setAuth;

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({
            ...prevFormData,
            [name]: value,
        }));
    }

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const { username, password } = formData;
        try{
            const response = await axios.post(LOGIN_URL,{
                username: username,
                password: password,
            }).then((response) => {
                let token: Token = response.data; 
                setAuth?.(token);
            });
            formData.username = "";
            formData.password = "";
        } catch(error){
            console.log(error);
        }
        };

        // useEffect(() => {
    //     let isMounted = true;
    //     const controller = new AbortController();

    //     const getUsers = async () => {
    //         try{
    //             const response = await axios.get("/users",{
    //                 signal: controller.signal,
    //             });
    //             console.log(response.data)
    //             if(isMounted){
    //                 setUsers(response.data);
    //             }
    //         }catch(error){
    //             console.log(error);
    //         }
    //     }
    //     getUsers();

    //     //Cleanup
    //     return() => {
    //         isMounted = false;
    //         controller.abort();
    //     }

    // },[]);
    

    return(
        <form onSubmit={handleSubmit}>
    <Typography align="center" gutterBottom fontSize={35}> Sign In</Typography>
            <TextField  onChange={handleChange} value={formData.username} label = "username" name="username" type = "text" fullWidth/>
            <TextField onChange={handleChange} value={formData.password} label = "Password" name="password" type = "password" fullWidth/>
            {/* <Link to = "/home" style = {{textDecoration: 'none'}}> */}
            <Button type = "submit" fullWidth variant = "contained" color = "primary" sx={{mt:3,mb:2}}>Sign In</Button>
            {/* </Link> */}
            <Link to = "/employeelogin" style = {{textDecoration: 'none'}}>
            <Button type = "submit" fullWidth variant = "contained" color = "success" sx={{mt:3,mb:2}}>Employee Sign In</Button>
            </Link>
            <Link to = "/signup" style = {{textDecoration: 'none'}}>
            <Button type = 'submit' fullWidth variant = "contained" color = "secondary" sx={{mt:3,mb:2}}>Sign Up</Button>
            </Link>
        </form>
    );
};


export default LoginForm;