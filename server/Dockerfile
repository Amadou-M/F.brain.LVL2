FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       libpq-dev \
    && pip install --no-cache-dir poetry==2.1.2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de dépendances
COPY pyproject.toml poetry.lock ./

# Empêcher Poetry de créer des environnements virtuels
ENV POETRY_VIRTUALENVS_CREATE=false

# Installer les dépendances sans installer le projet
RUN poetry install --no-root --no-interaction --no-ansi

# Copier le reste des fichiers de l'application
COPY . .

# Optionnel : exposer un port (ex: 8000 pour Django)
EXPOSE 8000

# Commande par défaut (à adapter selon ton framework)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

