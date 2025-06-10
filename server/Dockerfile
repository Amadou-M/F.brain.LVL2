FROM python:3.11

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Installer Poetry
RUN pip install poetry

# Empêcher poetry de créer un environnement virtuel
ENV POETRY_VIRTUALENVS_CREATE=false

# Copier uniquement les fichiers de dépendances en premier
COPY pyproject.toml poetry.lock* ./

# Installer les dépendances du projet
RUN poetry install --no-root --no-interaction --no-ansi


# Copier tout le reste de l’application
COPY . .

# Commande de démarrage par défaut (à adapter si besoin)
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
