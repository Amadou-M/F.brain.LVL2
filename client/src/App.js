import React, { useState } from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import BookList from './components/BookList';
import BorrowForm from './components/BorrowForm';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token') || '');

  const handleLogout = () => {
    localStorage.removeItem('token');
    setToken('');
  };

  return (
    <div className="app">
      <nav>
        <Link to="/">Accueil</Link> |{' '}
        {token ? (
          <>
            <Link to="/borrow">Emprunter</Link> |{' '}
            <button onClick={handleLogout}>Déconnexion</button>
          </>
        ) : (
          <>
            <Link to="/login">Connexion</Link> |{' '}
            <Link to="/register">Inscription</Link>
          </>
        )}
      </nav>
      <Routes>
        <Route path="/" element={<BookList token={token} />} />
        <Route path="/borrow" element={<BorrowForm token={token} />} />
        <Route path="/login" element={<LoginForm setToken={setToken} />} />
        <Route path="/register" element={<RegisterForm />} />
      </Routes>
    </div>
  );
}

export default App;