import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import LoginForm from './pages/LoginForm';
import SignUp from './pages/SignUp';
import Home from './pages/Home';
import EmployeeSignIn from './pages/EmployeeSignIn';
import EmployeeHome from './pages/EmployeeHome';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path = "/signup" element={<SignUp/>}/>
        <Route path = "/home" element={<Home/>}/>
        <Route path = "/employeelogin" element={<EmployeeSignIn/>}/>
        <Route path = "/employeehome" element={<EmployeeHome/>}/>
      </Routes>
    </Router>
  )
}

export default App

