import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { AuthProvider } from './context/authProvider'
import { UserProvider } from './context/userProvider';
import './index.css'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <AuthProvider initialAccessToken={null}>
      <UserProvider value={null}>
        <App />
      </UserProvider>
    </AuthProvider>
  </React.StrictMode>,
)
