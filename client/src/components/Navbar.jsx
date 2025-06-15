import React from "react";
import { Button } from "@/components/ui/button";
import { Book, UserCircle, LogOut } from "lucide-react";

const Navbar = () => {
  return (
    <nav className="flex items-center justify-between bg-blue-600 text-white p-4 shadow-md">
      <div className="flex items-center space-x-2">
        <Book className="w-6 h-6" />
        <span className="font-bold text-lg">Gestion de bibliothèque</span>
      </div>
      <div className="flex items-center space-x-4">
        <Button variant="ghost" className="text-white hover:bg-blue-500">
          <UserCircle className="w-5 h-5 mr-1" />
          Mon Compte
        </Button>
        <Button variant="outline" className="border-white text-white hover:bg-blue-500">
          <LogOut className="w-5 h-5 mr-1" />
          Déconnexion
        </Button>
      </div>
    </nav>
  );
};

export default Navbar;
