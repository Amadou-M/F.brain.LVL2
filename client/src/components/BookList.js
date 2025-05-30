import React, { useEffect, useState } from 'react';
import axios from 'axios';

const BookList = ({ token }) => {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const response = await axios.get('http://localhost/api/books/', {
          headers: token ? { Authorization: `Bearer ${token}` } : {},
        });
        setBooks(response.data);
      } catch (err) {
        setError('Erreur lors de la récupération des livres');
        console.error(err);
      }
    };
    fetchBooks();
  }, [token]);

  return (
    <div>
      <h2>Liste des livres</h2>
      {error && <p className="error">{error}</p>}
      <ul>
        {books.map(book => (
          <li key={book.id}>
            {book.title} ({book.publication_date}) -{' '}
            {book.is_available ? 'Disponible' : 'Emprunté'}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookList;