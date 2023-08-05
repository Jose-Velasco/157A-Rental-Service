import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import LoginForm from './pages/LoginForm';
import SignUp from './pages/SignUp';
import Home from './pages/Home';
import EmployeeSignIn from './pages/EmployeeSignIn';
import EmployeeHome from './pages/EmployeeHome';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import SearchMedia from './pages/SearchMedia';
import MediaDetail from './pages/MediaDetail';
import Inventory from './pages/Inventory';
import CartCheckout from './pages/CartCheckout';
import EmployeeList from './pages/EmployeeList';
import EditEmployee from './pages/EditEmployee';
import Transactions from './pages/Transactions';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path = "/signup" element={<SignUp/>}/>
        <Route path = "/home" element={<Home/>}/>
        <Route path = "/employeelogin" element={<EmployeeSignIn/>}/>
        <Route path = "/employeehome" element={<EmployeeHome/>}/>
        <Route path = "/search" element={<SearchMedia/>}/>
        <Route path = "/media-detail/:media_id" element={<MediaDetail/>}/>
        <Route path = "/inventory" element = {<Inventory/>}/>
        <Route path = "/cart-checkout" element = {<CartCheckout/>}/>
        <Route path = "/transactions" element = {<Transactions/>}/>
        <Route path = "/employee-list" element={<EmployeeList/>}/>
        <Route path = "/edit-employee/:employee_id" element={<EditEmployee/>}/>
      </Routes>
    </Router>
  )
}

export default App

