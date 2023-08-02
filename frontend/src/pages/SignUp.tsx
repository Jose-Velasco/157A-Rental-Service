import React, { useEffect } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import {Link, useNavigate} from "react-router-dom";
import axios from "../axios";






const SignUp:React.FC = () => {
    const [email, setEmail] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [birthday, setBirthday] = useState("");
    const [profilePicture] = useState("https://i.stack.imgur.com/l60Hf.png");
    const [age] = useState(30);
    const [phoneNumber, setPhoneNumber] = useState("");
    const [state, setState] = useState("");
    const [address] = useState([{}]);
    const [streetAddress, setStreetAddress] = useState("");
    const [city, setCity] = useState("");
    const [zipCode, setZipCode] = useState("");
    const [country, setCountry] = useState("");
    const [password, setPassword] = useState("");

            let isMounted = true;
            const controller = new AbortController();
            const navigate = useNavigate();
          
            const handleSubmit = (e: React.FormEvent) => {
                e.preventDefault();
                const data ={
                    first_name: firstName,
                    last_name: lastName,
                    birthday: birthday,
                    profile_pic_URL: profilePicture,
                    age: age,
                    phone_number: phoneNumber,
                    address : [
                        {
                        street: streetAddress,
                        city: city,
                        zip_code : zipCode,
                        country: country,
                        state:state,

                    }
                ],
                    email: [
                        {
                        email: email,
                    
                    }
                    
                ],
                username: email,
                password: password
                };
                console.log(data);
                try{
                    const response = axios.post("/user/customer", data).then((response) => { 
                      navigate("/")
                    });
                    console.log(response);
                    console.log(data)
                }
                catch(error){
                    console.log(error);
                }
                
        
            }
  



    return(
        <form style={{padding: "2rem"}}>
    <Typography align="center" gutterBottom fontSize={35}> Create Account</Typography>
            <TextField label = "First Name" type = "text" value ={firstName} onChange={(e) => setFirstName(e.target.value)}fullWidth/>
            <TextField label = "Last Name*" type = "text"value={lastName} onChange={(e) => setLastName(e.target.value)} fullWidth/>
            <TextField label = "Phone Number" type = "number"value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} fullWidth/>
            <TextField label = "Birthday" type = "text" fullWidth value={birthday} onChange={(e) => setBirthday(e.target.value)}/>
            <TextField label = "Street Address" type = "text"value={streetAddress} onChange={(e) => setStreetAddress(e.target.value)} fullWidth/>
            <TextField label = "City" type = "text" fullWidth value={city} onChange={(e) => setCity(e.target.value)}/>
            <TextField label = "State" type = "text" fullWidth value={state} onChange={(e) => setState(e.target.value)}/>
            <TextField label = "Zip Code" type ="number" fullWidth value ={zipCode} onChange={(e) => setZipCode(e.target.value)}/>
            <TextField label = "Country" type ="text" fullWidth value ={country} onChange={(e) => setCountry(e.target.value)}/>
            <TextField label = "Email" type = "email" value ={email} onChange={(e) => setEmail(e.target.value)}fullWidth />
            <TextField label = "Password" type = "password" fullWidth value ={password} onChange={(e) => setPassword(e.target.value)}/>
            <Button type = "submit" fullWidth variant = "contained" color = "primary" sx={{mt:3,mb:2}} onClick = {handleSubmit}>Create Account</Button>
        </form>
    );
};





export default SignUp;