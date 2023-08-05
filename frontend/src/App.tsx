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
      </Routes>
    </Router>
  )
}

export default App

