import React, { useEffect, useCallback, useState } from "react";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import { TextField, Typography, Button, Grid, Tooltip } from "@mui/material";
import { styled } from '@mui/material/styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import ReusableBar from "../components/ReusableBar";
import DeleteIcon from '@mui/icons-material/Delete';
import { User } from "../interfaces/user";

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

const EmployeeListUsers: React.FC = () => {
  const axiosPrivate = useAxiosPrivate();
  const [ users, setUsers ] = useState<User[]>([]);

  const deleteUser = async (user_id: number) => {
    try {
      await axiosPrivate.delete(`/user/customer/${user_id}`);
      // setUsers(users.filter((user) => user.user_id !== user_id));
      getUsers();
    } catch (err) {
      console.error(err);
    }
  };

  const getUsers = async () => {
    const response = await axiosPrivate.get<User[]>("/user/customer/");
    let users = response.data;
    if (users) {
      setUsers(users);
    };
  };

  useEffect(() => {
    getUsers();
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
          <StyledTableCell align="center">User ID</StyledTableCell>
          <StyledTableCell align="center">Name</StyledTableCell>
          <StyledTableCell align="center">Age</StyledTableCell>
          <StyledTableCell align="center">Birthday</StyledTableCell>
          <StyledTableCell align="center">Email</StyledTableCell>
          <StyledTableCell align="center">Phone number</StyledTableCell>
          <StyledTableCell align="center">Address</StyledTableCell>
          <StyledTableCell align="center">Delete</StyledTableCell>
          </TableRow>
      </TableHead>
      <TableBody>
          {users.map((row) => (
          <StyledTableRow key={row.user_id}>
              <StyledTableCell component="th" scope="row">
                  <img style={{height: 80}} src={row.profile_pic_URL}/>
              </StyledTableCell>
              <StyledTableCell align="center">{row.user_id}</StyledTableCell>
              <StyledTableCell align="center">{row.first_name}, {row.last_name}</StyledTableCell>
              <StyledTableCell align="center">{row.age}</StyledTableCell>
              <StyledTableCell align="center">{row.birthday.toString()}</StyledTableCell>
              <StyledTableCell align="center">{row.email[0]?.email}</StyledTableCell>
              <StyledTableCell align="center">{row.phone_number}</StyledTableCell>
              <StyledTableCell align="center">{row.address[0]?.street} {row.address[0]?.city} {row.address[0]?.zip_code} {row.address[0]?.state} {row.address[0]?.country}</StyledTableCell>
              <StyledTableCell align="center">
                  <Button onClick={() => deleteUser(row.user_id ? row.user_id : -1)} size="large">
                       <DeleteIcon fontSize="large" color="error" />
                  </Button>
              </StyledTableCell>
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

export default EmployeeListUsers;