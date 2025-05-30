import React, { useState } from 'react';
import axios from 'axios';

const BorrowForm = ({ token }) => {
  const [bookId, setBookId] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        'http://localhost/api/borrows/',
        { book: bookId },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setMessage('Livre emprunté avec succès !');
      setBookId('');
    } catch (err) {
      setError('Erreur lors de l\'emprunt');
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Emprunter un livre</h2>
      {message && <p className="success">{message}</p>}
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSubmit}>
        <label>
          ID du livre :
          <input
            type="number"
            value={bookId}
            onChange={(e) => setBookId(e.target.value)}
            required
          />
        </label>
        <button type="submit">Emprunter</button>
      </form>
    </div>
  );
};

export default BorrowForm;