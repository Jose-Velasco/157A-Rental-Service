import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import LoginForm from './pages/LoginForm';
import SignUp from './pages/SignUp';
import Home from './pages/Home';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path = "/signup" element={<SignUp/>}/>
        <Route path = "/home" element={<Home/>}/>
      </Routes>
    </Router>
  )
}

export default App

