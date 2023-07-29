import React from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import {Theme, makeStyles,createTheme} from "@mui/material/styles";

const LoginForm:React.FC = () => {
    return(
        <form>
    <Typography align="center" gutterBottom fontSize={35}> Sign In</Typography>
            <TextField label = "Email" type = "email" fullWidth/>
            <TextField label = "Password*" type = "password" fullWidth/>
            <Button type = "submit" fullWidth variant = "contained" color = "primary" sx={{mt:3,mb:2}}>Sign In</Button>
            <Button type = 'submit' fullWidth variant = "contained" color = "secondary" sx={{mt:3,mb:2}}>Sign Up</Button>
        </form>
    );
};


export default LoginForm;