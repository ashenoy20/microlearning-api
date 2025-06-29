import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Login from './components/login/login';
import Register from './components/register/register';

const App = () => {
  const handleLogin = (credentials) => {
    console.log('Login attempt:', credentials);
  };

  const handleRegister = (data) => {
    console.log('Register attempt:', data);
  };

  return (
    <Routes>
      <Route path="/" element={<h1>Hello World</h1>} />
      <Route path="/login" element={<Login onLogin={handleLogin} />} />
      <Route path="/register" element={<Register onRegister={handleRegister} />} />
    </Routes>
  );
};

export default App;
