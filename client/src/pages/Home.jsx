// Home.jsx
import React from "react";
import Navbar from "./Navbar";

const Home = () => {
  return (
    <div>
      <Navbar />
      <main className="p-6">
        <h1 className="text-3xl font-bold mb-4">Bienvenue à la bibliothèque en ligne</h1>
        <p className="text-lg text-gray-700">Consultez, empruntez et gérez vos livres en toute simplicité.</p>
      </main>
    </div>
  );
};

export default Home;
