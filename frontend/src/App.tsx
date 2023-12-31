import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import LoginForm from './pages/LoginForm';
import SignUp from './pages/SignUp';
import Home from './pages/Home';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import SearchMedia from './pages/SearchMedia';
import MediaDetail from './pages/MediaDetail';
import Inventory from './pages/Inventory';
import CartCheckout from './pages/CartCheckout';
import UpdateUser from './pages/UpdateUser';
import EmployeeList from './pages/EmployeeList';
import EditEmployee from './pages/EditEmployee';
import Transactions from './pages/Transactions';
import EmployeeListUsers from './pages/EmployeeListUsers';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path = "/signup" element={<SignUp/>}/>
        <Route path = "/home" element={<Home/>}/>
        <Route path = "/search" element={<SearchMedia/>}/>
        <Route path = "/media-detail/:media_id" element={<MediaDetail/>}/>
        <Route path = "/inventory" element = {<Inventory/>}/>
        <Route path = "/cart-checkout" element = {<CartCheckout/>}/>
        <Route path = "/update-user" element = {<UpdateUser/>}/>
        <Route path = "/transactions" element = {<Transactions/>}/>
        <Route path = "/employee-list" element={<EmployeeList/>}/>
        <Route path = "/edit-employee/:employee_id" element={<EditEmployee/>}/>
        <Route path = "/employee-list-user" element={<EmployeeListUsers/>}/>
      </Routes>
    </Router>
  )
}

export default App

