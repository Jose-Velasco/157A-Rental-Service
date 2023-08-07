import React, { useEffect } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import ReusableBar from "../components/ReusableBar";
import useUser  from "../hooks/useUser";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import {Link, Navigate, useNavigate} from "react-router-dom";
import { useParams } from 'react-router-dom';
import axios from "../axios";
import { User } from "../interfaces/user";


const UpdateUser: React.FC = () => {
    
    const userContextValue = useUser();
    const axiosPrivate = useAxiosPrivate();
    const navigate = useNavigate();
    const getUser = userContextValue?.user;
    const [user, setUser] = useState<User>();
    const [email, setEmail] = useState("");
    const { user_id } = useParams<{ user_id: string }>();
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [birthday, setBirthday] = useState(""); // [year, month, day
    const [age, setAge] = useState(0);
    const [profilePicture] = useState("https://i.stack.imgur.com/l60Hf.png");
    const [phoneNumber, setPhoneNumber] = useState("");
    const [state, setState] = useState("");
    const [address] = useState([{}]);
    const [streetAddress, setStreetAddress] = useState("");
    const [city, setCity] = useState("");
    const [zipCode, setZipCode] = useState("");
    const [country, setCountry] = useState("");
    const [ isUpdatingUser, setIsUpdatingCustomer] = useState<boolean>(false);


    const setExistingUserData = () => {
        if (user) {
            setFirstName(user.first_name);
            setLastName(user.last_name);
            setBirthday(String(user.birthday));
            setPhoneNumber(String(user.phone_number));
            setStreetAddress(user.address[0].street);
            setCity(user.address[0].city);
            setState(user.address[0].state);
            setZipCode(String(user.address[0].zip_code));
            setCountry(user.address[0].country);
            setEmail(user.email[0].email);
            setAge(user.age);
        }
 
    };


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
        
        };
        console.log(data);
        try{
            const response = axiosPrivate.put(`/user/customer/${getUser?.user_id}`, data).then((response) => { 
                navigate("/home");
            });
            console.log(response);
            console.log(data)
            
        }
        catch(error){
            console.log(error);
        }
        

    };


    const getCustomer = async () => {
        try {
            const response = await axiosPrivate.get(`/user/customer/${getUser?.user_id}`);
            setUser(response.data);
        } catch (error) {
            console.log(error);
        }
    };


    const calculateAge =  async (birthday: string) => {
        const today = new Date();
        const birthDate = new Date(birthday);
        let age = today.getFullYear() - birthDate.getFullYear();
        const month = today.getMonth() - birthDate.getMonth();
        if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        console.log(age);
        setAge(age);
    };

    



    useEffect(() => {
        getCustomer();
    }, []);

    useEffect(() => {
        setExistingUserData();
        setIsUpdatingCustomer(checkisUpdatingUser());
    }, [user]);

      useEffect(() => {   
        calculateAge(birthday);
    }
    , [birthday]);
    const checkisUpdatingUser = () => user_id !== undefined && user_id !== "-1";




    return(
        <form style={{padding: "2rem"}}>
         <div style={{marginBottom: 75}}>
                <ReusableBar title = {"Update "+ `${getUser?.first_name}`} showInventoryIcon = {false} />
            </div>
            <Typography align="center" gutterBottom fontSize={35}>Update Account</Typography>
            <TextField label = "First Name" type = "text" value ={firstName} onChange={(e) => setFirstName(e.target.value)}fullWidth/>
            <TextField label = "Last Name*" type = "text"value={lastName} onChange={(e) => setLastName(e.target.value)} fullWidth/>
            <TextField label = "Phone Number" type = "number"value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} fullWidth/>
            <TextField label = "" type = "Date" fullWidth value={birthday} onChange={(e) => setBirthday(e.target.value)}/>
            <TextField label = "Street Address" type = "text"value={streetAddress} onChange={(e) => setStreetAddress(e.target.value)} fullWidth/>
            <TextField label = "City" type = "text" fullWidth value={city} onChange={(e) => setCity(e.target.value)}/>
            <TextField label = "State" type = "text" fullWidth value={state} onChange={(e) => setState(e.target.value)}/>
            <TextField label = "Zip Code" type ="number" fullWidth value ={zipCode} onChange={(e) => setZipCode(e.target.value)}/>
            <TextField label = "Country" type ="text" fullWidth value ={country} onChange={(e) => setCountry(e.target.value)}/>
            <TextField label = "Email" type = "email" value ={email} onChange={(e) => setEmail(e.target.value)}fullWidth />
            <Button type = "submit" fullWidth variant = "contained" color = "primary" sx={{mt:3,mb:2}} onClick = {handleSubmit}>Update Profile!</Button>


        </form>




    );



}
export default UpdateUser;