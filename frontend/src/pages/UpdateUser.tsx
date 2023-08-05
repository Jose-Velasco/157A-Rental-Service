import React, { useEffect } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import ReusableBar from "../components/ReusableBar";
import useUser  from "../hooks/useUser";
import axios from "../axios";
import {Link, useNavigate} from "react-router-dom";

const UpdateUser: React.FC = () => {
    
    const userContextValue = useUser();
    const getUser = userContextValue?.user;

    const [email, setEmail] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [birthday, setBirthday] = useState(Date); // [year, month, day
    const [age] = useState(0);
    const [profilePicture] = useState("https://i.stack.imgur.com/l60Hf.png");
    const [phoneNumber, setPhoneNumber] = useState("");
    const [state, setState] = useState("");
    const [address] = useState([{}]);
    const [streetAddress, setStreetAddress] = useState("");
    const [city, setCity] = useState("");
    const [zipCode, setZipCode] = useState("");
    const [country, setCountry] = useState("");
    const [password, setPassword] = useState("");
    const [userName, setUserName] = useState("");


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
        username: userName,
        password: password
        };
        console.log(data);
        try{
            const response = axios.put("/user/customer", data).then((response) => { 
            });
            console.log(response);
            console.log(data)
        }
        catch(error){
            console.log(error);
        }
        

    };

    const initializeProfile = () => {
        setFirstName(getUser?.first_name ? getUser.first_name : "");
        setLastName(getUser?.last_name ? getUser.last_name : "");
        setBirthday(getUser?.birthday ? getUser.birthday : Date);
        setPhoneNumber(getUser?.phone_number ? getUser.phone_number : "");
        setStreetAddress(getUser?.address[0].street ? getUser.address[0].street : "");
        setCity(getUser?.address[0].city ? getUser.address[0].city : "");
        setZipCode(getUser?.address[0].zip_code ? getUser.address[0].zip_code : "");
        setCountry(getUser?.address[0].country ? getUser.address[0].country : "");
        setState(getUser?.address[0].state ? getUser.address[0].state : "");
        setEmail(getUser?.email[0].email ? getUser.email[0].email : "");
        setUserName(getUser?.username ? getUser.username : "");
        setPassword(getUser?.password ? getUser.password : "");
    };


    return(
        <form style={{padding: "2rem"}}>
         <div style={{marginBottom: 75}}>
                <ReusableBar title = {"Update "+ `${getUser?.first_name}`} showInventoryIcon = {false} />
            </div>

            <Typography align="center" gutterBottom fontSize={35}> Create Account</Typography>
            <TextField label = "First Name" type = "text" value ={firstName} onChange={(e) => setFirstName(e.target.value)}fullWidth/>
            <TextField label = "Last Name*" type = "text"value={lastName} onChange={(e) => setLastName(e.target.value)} fullWidth/>
            <TextField label = "Phone Number" type = "number"value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} fullWidth/>
            <TextField label = "Birthday" type = "date" fullWidth value={birthday} onChange={(e) => setBirthday(e.target.value)}/>
            <TextField label = "Street Address" type = "text"value={streetAddress} onChange={(e) => setStreetAddress(e.target.value)} fullWidth/>
            <TextField label = "City" type = "text" fullWidth value={city} onChange={(e) => setCity(e.target.value)}/>
            <TextField label = "State" type = "text" fullWidth value={state} onChange={(e) => setState(e.target.value)}/>
            <TextField label = "Zip Code" type ="number" fullWidth value ={zipCode} onChange={(e) => setZipCode(e.target.value)}/>
            <TextField label = "Country" type ="text" fullWidth value ={country} onChange={(e) => setCountry(e.target.value)}/>
            <TextField label = "Email" type = "email" value ={email} onChange={(e) => setEmail(e.target.value)}fullWidth />
            <TextField label = "Username" type = "text" fullWidth value ={userName} onChange={(e) => setUserName(e.target.value)}/>
            <TextField label = "Password" type = "password" fullWidth value ={password} onChange={(e) => setPassword(e.target.value)}/>
            <Button type = "submit" fullWidth variant = "contained" color = "primary" sx={{mt:3,mb:2}} onClick = {handleSubmit}>Update Profile!</Button>


        </form>




    );



}
export default UpdateUser;