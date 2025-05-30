# Utiliser une image Node.js légère
FROM node:20

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY package.json yarn.lock ./

# Installer les dépendances
RUN yarn install

# Copier le reste du projet
COPY . .

# Exposer le port pour le serveur de développement
EXPOSE 5173

# Commande pour lancer le serveur de développement
CMD ["yarn", "dev"]