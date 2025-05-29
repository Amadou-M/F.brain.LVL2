# Étape 1 : Image Python minimale
FROM python:3.11-slim

# Étape 2 : Définir le répertoire de travail
WORKDIR /app

# Étape 3 : Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Étape 4 : Installer Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Étape 5 : Empêcher Poetry de créer un venv
ENV POETRY_VIRTUALENVS_CREATE=false \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Étape 6 : Copier les fichiers de dépendances
COPY pyproject.toml poetry.lock ./

# Étape 7 : Installer les dépendances (hors projet)
RUN poetry install --no-root --no-interaction --no-ansi

# Étape 8 : Copier le reste du projet
COPY . .

# Étape 9 : Exposer le port pour Gunicorn ou Django dev server
EXPOSE 8000

# Étape 10 : Commande par défaut (à surcharger dans docker-compose)
CMD ["gunicorn", "server_config.wsgi:application", "--bind", "0.0.0.0:8000"]
