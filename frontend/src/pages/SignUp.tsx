import React, { useEffect } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import {Link} from "react-router-dom";
import axios from "../axios";





const SignUp:React.FC = () => {
    const [email, setEmail] = useState("");
    const [emails, setEmails] = useState([]); 
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [birthday, setBirthday] = useState("");
    const [profilePicture] = useState("https://i.stack.imgur.com/l60Hf.png");
    const [age] = useState(30);
    const [phoneNumber, setPhoneNumber] = useState("");
    const [address, setAddress] = useState();
    const [streetAddress, setStreetAddress] = useState("");
    const [city, setCity] = useState("");
    const [zipCode, setZipCode] = useState("");
    const [password, setPassword] = useState("");

            let isMounted = true;
            const controller = new AbortController();

            const generateUser = async () => {  
                try{
                    const response = await axios.post("/user/customer",{
                        signal: controller.signal,
                    });
                console.log(response.data)
                    if(isMounted){
                        firstName
                        lastName
                        birthday
                        profilePicture
                        age
                        phoneNumber
                        address

                    }
                }catch(error){
                    console.log(error);
                }
        }
        generateUser();
  



    return(
        <form>
    <Typography align="center" gutterBottom fontSize={35}> Create Account</Typography>
            <TextField label = "First Name" type = "text" value ={firstName} onChange={(e) => setFirstName(e.target.value)}fullWidth/>
            <TextField label = "Last Name*" type = "text"value={lastName} onChange={(e) => setLastName(e.target.value)} fullWidth/>
            <TextField label = "" type = "date"value={birthday} onChange={(e) => setBirthday(e.target.value)} fullWidth/>
            <TextField label = "Phone Number" type = "text"value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} fullWidth/>
            <TextField label = "Street Address" type = "text"value={streetAddress} onChange={(e) => setStreetAddress(e.target.value)} fullWidth/>
            <TextField label = "City" type = "text" fullWidth value={city} onChange={(e) => setCity(e.target.value)}/>
            <TextField label = "Zip Code" type = "text" fullWidth value ={zipCode} onChange={(e) => setZipCode(e.target.value)}/>
            <TextField label = "Email" type = "email" value ={email} onChange={(e) => setEmail(e.target.value)}fullWidth />
            <TextField label = "Password*" type = "password" fullWidth value ={password} onChange={(e) => setPassword(e.target.value)}/>
            <Link to = "/" style = {{textDecoration: 'none'}}>
            <Button type = "submit" fullWidth variant = "contained" color = "primary" sx={{mt:3,mb:2}} onClick = {generateUser}>Create Account</Button>
            </Link>
        </form>
    );
};





export default SignUp;