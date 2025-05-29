# Étape 1 : Build de l'app frontend
FROM node:20-alpine AS build

WORKDIR /app

# Copier uniquement les fichiers de dépendances
COPY package.json yarn.lock ./

# Installer les dépendances avec Yarn
RUN yarn install --frozen-lockfile

# Copier le reste de l'app
COPY . .

# Compiler l'app pour la production
RUN yarn build

# Étape 2 : Serveur web statique avec Nginx
FROM nginx:alpine

# Supprimer la config Nginx par défaut
RUN rm /etc/nginx/conf.d/default.conf

# Ajouter ta propre config compatible SPA
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copier le build React vers Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Exposer le port web
EXPOSE 80

# Lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
