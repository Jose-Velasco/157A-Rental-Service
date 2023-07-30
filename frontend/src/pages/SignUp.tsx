import React, { useEffect } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import {Link} from "react-router-dom";





const SignUp:React.FC = () => {

    return(
        <form>
    <Typography align="center" gutterBottom fontSize={35}> Create Account</Typography>
            <TextField label = "Email" type = "email" fullWidth />
            <TextField label = "First Name" type = "password" fullWidth/>
            <TextField label = "Last Name*" type = "password" fullWidth/>
            <TextField label = "Phone Number" type = "password" fullWidth/>
            <TextField label = "Street Address" type = "password" fullWidth/>
            <TextField label = "City" type = "password" fullWidth/>
            <TextField label = "Zip Code" type = "password" fullWidth/>
            <TextField label = "Password*" type = "password" fullWidth/>
            <Link to = "/" style = {{textDecoration: 'none'}}>
            <Button type = "submit" fullWidth variant = "contained" color = "primary" sx={{mt:3,mb:2}}>Create Account</Button>
            </Link>
        </form>
    );
};





export default SignUp;