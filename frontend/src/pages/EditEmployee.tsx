import React, { useEffect, useCallback, useState } from "react";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import { Employee, EmployeeTypes } from "../interfaces/user";
import ReusableBar from "../components/ReusableBar";
import { Button } from "@mui/material";
import { useNavigate, Link } from "react-router-dom";
import { TextField, Typography} from "@mui/material";
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormLabel from '@mui/material/FormLabel';
import { useParams } from 'react-router-dom';



const textfieldStyle = {
    marginBottom: 20,
};

const EmployeeList: React.FC = () => {
    const axiosPrivate = useAxiosPrivate();
    const { employee_id } = useParams<{ employee_id: string }>();
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [ username, setUsername] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [birthday, setBirthday] = useState("");
    const [profilePicture] = useState("https://i.stack.imgur.com/l60Hf.png");
    const [age] = useState(30);
    const [phoneNumber, setPhoneNumber] = useState("");
    const [state, setState] = useState("");
    const [streetAddress, setStreetAddress] = useState("");
    const [city, setCity] = useState("");
    const [zipCode, setZipCode] = useState("");
    const [country, setCountry] = useState("");
    const [password, setPassword] = useState("");
    
    // extra employee fields
    const [ ssn, setSsn] = useState("");
    const [ salary, setSalary] = useState("");
    const [ startDate, setStartDate] = useState("");
    const [ employeeType, setEmployeeType] = useState<EmployeeTypes>(EmployeeTypes.Manager);
    // if there is an existing employee else it will be undefined
    const [ employee, setEmployee] = useState<Employee>();
    const [ isUpdatingEmployee, setIsUpdatingEmployee] = useState<boolean>(false);


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
        username: username,
        password: password,
        ssn: ssn,
        salary: salary,
        start_date: startDate,
        employee_type: employeeType,
        };
        if (employee_id && employee_id !== "-1") {
            try{
                // update existing employee
                const response = axiosPrivate.put(`/user/employee/${employee_id}`, data).then((response) => { 
                  navigate("/employee-list")
                });
            }
            catch(error){
                console.log(error);
            }
        } else {
            try{
                // create new employee
                const response = axiosPrivate.post("/user/employee/", data).then((response) => { 
                  navigate("/employee-list")
                });
            }
            catch(error){
                console.log(error);
            }
        }
    }

    const setExistingEmployeeData = () => {
        if (employee_id === undefined || employee_id === "-1") {
            return;
        }
        if (employee) {
            setFirstName(employee.first_name);
            setLastName(employee.last_name);
            setBirthday(String(employee.birthday));
            setPhoneNumber(String(employee.phone_number));
            setStreetAddress(employee.address[0].street);
            setCity(employee.address[0].city);
            setState(employee.address[0].state);
            setZipCode(String(employee.address[0].zip_code));
            setCountry(employee.address[0].country);
            setEmail(employee.email[0].email);
            setSsn(String(employee.ssn));
            setSalary(String(employee.salary));
            setStartDate(String(employee.start_date));
            if (employee && employee.employee_type !== undefined) {
                setEmployeeType(EmployeeTypes[employee.employee_type]);
            } else {
                setEmployeeType(EmployeeTypes.Manager);
            }
        }
    };

    const getEmployee = async () => {
        if (employee_id === undefined || employee_id === "-1") {
            return;
        }
        try {
            const response = await axiosPrivate.get(`/user/employee/${employee_id}`);
            setEmployee(response.data);
            setExistingEmployeeData();
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        getEmployee();
    }, []);

    useEffect(() => {
        setExistingEmployeeData();
        setIsUpdatingEmployee(checkIsUpdatingEmployee());
    }, [employee]);

    const checkIsUpdatingEmployee = () => employee_id !== undefined && employee_id !== "-1";

    return (
        <form style={{padding: "2rem"}}>
        <Typography align="center" gutterBottom fontSize={35}> { employee_id !== "-1"? "Update Employee Account" : "Create Account"}</Typography>
        <div>
                <TextField style={textfieldStyle} label = "First Name" type = "text" value ={firstName} onChange={(e) => setFirstName(e.target.value)}fullWidth/>
                <TextField style={textfieldStyle} label = "Last Name*" type = "text"value={lastName} onChange={(e) => setLastName(e.target.value)} fullWidth/>
                <TextField style={textfieldStyle} label = "Phone Number" type = "number"value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} fullWidth/>
                <TextField style={textfieldStyle} label = "Birthday" type = "date" fullWidth value={birthday} onChange={(e) => setBirthday(e.target.value)}/>
                <TextField style={textfieldStyle} label = "Street Address" type = "text"value={streetAddress} onChange={(e) => setStreetAddress(e.target.value)} fullWidth/>
                <TextField style={textfieldStyle} required label = "City" type = "text" fullWidth value={city} onChange={(e) => setCity(e.target.value)}/>
                <TextField style={textfieldStyle} required label = "State" type = "text" fullWidth value={state} onChange={(e) => setState(e.target.value)}/>
                <TextField style={textfieldStyle} label = "Zip Code" type ="number" fullWidth value ={zipCode} onChange={(e) => setZipCode(e.target.value)}/>
                <TextField style={textfieldStyle} label = "Country" type ="text" fullWidth value ={country} onChange={(e) => setCountry(e.target.value)}/>
                <TextField style={textfieldStyle} required label = "Email" type = "email" value ={email} onChange={(e) => setEmail(e.target.value)}fullWidth />
                <TextField style={textfieldStyle} required disabled={isUpdatingEmployee} label = "username" type = "text" fullWidth value ={username} onChange={(e) => setUsername(e.target.value)}/>
                <TextField style={textfieldStyle} required disabled={isUpdatingEmployee} label = "Password" type = "password" fullWidth value ={password} onChange={(e) => setPassword(e.target.value)}/>
                <TextField style={textfieldStyle} required label = "SSN" type = "number" fullWidth value ={ssn} onChange={(e) => setSsn(e.target.value)}/>
                <TextField style={textfieldStyle} label = "Salary" type = "number" fullWidth value ={salary} onChange={(e) => setSalary(e.target.value)}/>
                <TextField style={textfieldStyle} label = "Start Date" type = "date" fullWidth value ={startDate} onChange={(e) => setStartDate(e.target.value)}/>
        </div>
                <FormLabel id="demo-row-radio-buttons-group-label">Employee Type</FormLabel>
                <RadioGroup
                    value={employeeType}
                    onChange={(e) => setEmployeeType(e.target.value as EmployeeTypes)}
                    row
                    aria-labelledby="demo-row-radio-buttons-group-label"
                    name="row-radio-buttons-group">
                    <FormControlLabel value={EmployeeTypes.Manager} control={<Radio />} label={EmployeeTypes.Manager} />
                    <FormControlLabel value={EmployeeTypes.Admin} control={<Radio />} label={EmployeeTypes.Admin} />
                </RadioGroup>
                <Button style={{marginRight: 50}} type = "submit"  variant = "contained" color = "success" sx={{mt:3,mb:2}} onClick = {handleSubmit}>Submit</Button>
                <Link to="/employee-list">
                <Button type = "button"  variant = "contained" color = "error" sx={{mt:3,mb:2}}>Cancel</Button>
                </Link>
        </form>
    );
};

export default EmployeeList;