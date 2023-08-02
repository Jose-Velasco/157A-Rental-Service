import React, { useEffect, useCallback } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "../axios";
import useAuth from "../hooks/useAuth";
import useUser  from "../hooks/useUser";
import { Token } from "../interfaces/token";
import { User } from "../interfaces/user";

const LOGIN_URL = "/auth/token/";

interface Cart {
    user_id: number;
    cart_id: number;
}

const LoginForm:React.FC = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        username: "",
        password: "",
    });
    const authContextValue = useAuth();
    const setAuth = authContextValue?.setAuth;
    const userContextValue = useUser();
    const setUser = userContextValue?.setUser;
    const auth = authContextValue?.auth;

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({
            ...prevFormData,
            [name]: value,
        }));
    }

    const getUserInfo = async (token: Token) => {
        try {
            const response = await axios.get("/auth/users/me/", 
            {
                headers: {
                    Authorization: `Bearer ${token.access_token}`,
                },
            })
            let user: User = response.data;
            const cart_response = await axios.get(`/cart/${user.user_id}`, 
            {
                headers: {
                    Authorization: `Bearer ${token.access_token}`,
                },
            });
            let cart: Cart = cart_response.data;
            user.cart_id = cart.cart_id;
            setUser?.(user);
            navigate("/home");
        } catch (error) {
            console.log(error);
        }
    };

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const { username, password } = formData;
        try{
            const response = await axios.postForm(LOGIN_URL,{
                username: username,
                password: password,
            })
            let token: Token = response.data;
            setAuth?.(token);
            setFormData({
                username: "",
                password: "",
            });
            getUserInfo(token);
            console.log(auth);
        } catch(error){
            console.log(error);
        }
        };

    return(
        <div style={{display: "flex", justifyContent: "center", alignItems: "center", height: "100vh"}}>
            <form onSubmit={handleSubmit} >
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
        </div>
    );
};


export default LoginForm;