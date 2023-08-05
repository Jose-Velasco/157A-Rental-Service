import React, { useEffect, useCallback, useState } from "react";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import { Employee } from "../interfaces/user";
import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import ReusableBar from "../components/ReusableBar";
import { Button } from "@mui/material";
import CreateIcon from '@mui/icons-material/Create';
import { useNavigate } from "react-router-dom";
import AddCircleIcon from '@mui/icons-material/AddCircle';
import DeleteIcon from '@mui/icons-material/Delete';


const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
      backgroundColor: "#CCDEFF",
    },
    [`&.${tableCellClasses.body}`]: {
      fontSize: 14,
    },
  }));

    
const StyledTableRow = styled(TableRow)(({ theme }) => ({
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
    // hide last border
    '&:last-child td, &:last-child th': {
      border: 0,
    },
  }));

const EmployeeList: React.FC = () => {
    const axiosPrivate = useAxiosPrivate();
    const navigate = useNavigate();
    const [employees, setEmployees] = useState<Employee[]>([]);

    const getEmployees = async () => {
        const response = await axiosPrivate.get<Employee[]>("/user/employee/");
        let employees = response.data;
        if (employees) {
            setEmployees(employees);
        };
    };

    const onCreateEmployee = async () => {
        navigate(`/edit-employee/-1`);
    };

    const editEmployee = async (user_id: number) => {
        navigate(`/edit-employee/${user_id}`);
    };

    const deleteEmployee = async (user_id: number) => {
        const response = await axiosPrivate.delete(`/user/employee/${user_id}`);
        if (response.status === 200) {
            getEmployees();
        };
    };

    useEffect(() => {
        getEmployees();
    }, []);

    return (
        <div>
        <div style={{marginBottom: 75}}>
            <ReusableBar title = "Search Page"  showInventoryIcon = {false} />
        </div>
        <div>
        <TableContainer component={Paper}>
        <Table sx={{ minWidth: 700 }} aria-label="customized table">
        <TableHead>
            <TableRow>
            <StyledTableCell>Picture</StyledTableCell>
            <StyledTableCell align="center">Name</StyledTableCell>
            <StyledTableCell align="center">Phone number</StyledTableCell>
            <StyledTableCell align="center">Salary</StyledTableCell>
            <StyledTableCell align="center">Start Date</StyledTableCell>
            <StyledTableCell align="center">Employee Type</StyledTableCell>
            <StyledTableCell align="center">Edit</StyledTableCell>
            <StyledTableCell align="center">Delete</StyledTableCell>
            <StyledTableCell align="right">
                <Button style={{padding: 0}} onClick={onCreateEmployee} size="large">
                    <AddCircleIcon style={{fontSize: 60}} color="success" />
                </Button>
            </StyledTableCell>
            </TableRow>
        </TableHead>
        <TableBody>
            {employees.map((row) => (
            <StyledTableRow key={row.user_id}>
                <StyledTableCell component="th" scope="row">
                    <img style={{height: 80}} src={row.profile_pic_URL}/>
                </StyledTableCell>
                <StyledTableCell align="center">{row.first_name}, {row.last_name}</StyledTableCell>
                <StyledTableCell align="center">{row.phone_number}</StyledTableCell>
                <StyledTableCell align="center">{row.salary}</StyledTableCell>
                <StyledTableCell align="center">{row.start_date?.toString()}</StyledTableCell>
                <StyledTableCell align="center">{row.employee_type}</StyledTableCell>
                <StyledTableCell align="center">
                    <Button onClick={() => editEmployee(row.user_id ? row.user_id : -1)} size="large">
                         <CreateIcon fontSize="large" color="success" />
                    </Button>
                </StyledTableCell>
                <StyledTableCell align="right">
                    <Button onClick={() => deleteEmployee(row.user_id ? row.user_id : -1)} size="large">
                         <DeleteIcon fontSize="large" color="error" />
                    </Button>
                </StyledTableCell>
                <StyledTableCell align="right"></StyledTableCell>
            </StyledTableRow>
            ))}
        </TableBody>
        </Table>
        </TableContainer>
        <br />
        </div>
    </div>
    );
};

export default EmployeeList;