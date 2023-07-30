import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import LoginForm from './pages/LoginForm';
import SignUp from './pages/SignUp';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';

function App() {
  const [count, setCount] = useState(0);
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);


  useEffect(() => {
    fetch("http://localhost:8080/welcome")
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setItems(result);
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [])


  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path = "/signup" element={<SignUp/>}/>
      </Routes>
    </Router>
  )
}

export default App
