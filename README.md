📚 Gestion_de_bibliothèque

Bienvenue dans Gestion_de_bibliothèque, une application moderne pour gérer une bibliothèque en ligne. Ce projet utilise une stack DevOps complète avec React pour le frontend, Django pour le backend, Celery pour les tâches asynchrones, Docker pour le déploiement, Nginx comme proxy, et Prometheus/Grafana pour le monitoring. Une pipeline CI/CD est configurée via GitHub Actions avec deux branches : dev pour le développement et master pour la production.

🚀 Fonctionnalités





Liste des livres disponibles : Affiche les livres avec leur titre et date de publication.



Gestion des emprunts : Permet aux utilisateurs d'emprunter et de rendre des livres.



Authentification : Pages pour l'authentification des utilisateurs et des administrateurs.



Monitoring : Suivi des performances avec Prometheus et visualisation via Grafana.



Tâches asynchrones : Gestion des notifications ou tâches lourdes via Celery et RabbitMQ.



CI/CD : Pipeline automatisée avec GitHub Actions pour tests et déploiement.

📁 Structure du projet

f_brain/
├── client/                 # Frontend React
├── server/                 # Backend Django
├── proxy/                  # Configuration Nginx
├── docker-compose.yml      # Configuration Docker
├── .env                    # Variables d'environnement
├── prometheus.yml          # Configuration Prometheus
├── grafana.ini             # Configuration Grafana
└── README.md               # Documentation (ce fichier)

🛠️ Prérequis





Docker & Docker Compose



Node.js (pour le développement local du frontend)



Python 3.11+ (pour le développement local du backend)



Poetry (pour la gestion des dépendances Python)



Yarn (pour le frontend React)



Un compte GitHub pour la configuration CI/CD

⚙️ Installation

1. Cloner le dépôt

git clone https://github.com/<votre-username>/gestion-de-bibliotheque.git
cd gestion-de-bibliotheque

2. Configurer les variables d'environnement

Créez un fichier .env à la racine du projet avec les variables suivantes :

POSTGRES_DB=devops_db
POSTGRES_USER=devops_user
POSTGRES_PASSWORD=devops_pass
POSTGRES_HOST=db
DJANGO_SECRET_KEY=un_secret_costaud
CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
DJANGO_DEBUG=True
GF_SECURITY_ADMIN_USER=admin
GF_SECURITY_ADMIN_PASSWORD=admin

3. Lancer les services avec Docker Compose

docker-compose up --build

Cela construit et lance les services suivants :





Frontend : React sur http://localhost:80



Backend : Django sur http://localhost/api/



Proxy : Nginx sur http://localhost



Database : PostgreSQL



Message Broker : RabbitMQ sur http://localhost:15672 (user: guest, pass: guest)



Monitoring : Prometheus sur http://localhost:9090, Grafana sur http://localhost:3000

4. Accéder à l'application





Frontend : Ouvrez http://localhost pour voir l'interface React.



Admin Django : Accédez à http://localhost/api/admin/ après avoir créé un superutilisateur :

docker-compose exec web python manage.py createsuperuser



Grafana : Connectez-vous à http://localhost:3000 (user: admin, pass: admin) pour configurer les dashboards.



Prometheus : Vérifiez les métriques sur http://localhost:9090.

🧑‍💻 Développement local

Frontend (React)





Naviguez dans le dossier client :

cd client
yarn install
yarn dev



Le frontend sera accessible sur http://localhost:5173.

Backend (Django)





Naviguez dans le dossier server :

cd server
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver



Le backend sera accessible sur http://localhost:8000.

Créer une application Django pour la gestion de bibliothèque





Créez une app Django :

poetry run python manage.py startapp library



Ajoutez library à INSTALLED_APPS dans server/server_config/settings.py.



Configurez les modèles dans server/library/models.py :

from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"



Créez et appliquez les migrations :

poetry run python manage.py makemigrations
poetry run python manage.py migrate

Authentification





Utilisez le système d'authentification intégré de Django pour gérer les utilisateurs et admins.



Configurez les vues et templates dans server/library/views.py et client/src pour les pages de connexion/inscription.

📊 Monitoring





Prometheus : Configurez prometheus.yml pour scraper les métriques Django :

scrape_configs:
  - job_name: 'django'
    static_configs:
      - targets: ['web:8000']



Grafana : Ajoutez Prometheus comme source de données et créez des dashboards pour visualiser les métriques (CPU, mémoire, requêtes API).

🚀 CI/CD avec GitHub Actions

Le projet utilise deux branches :





dev : Pour le développement et les tests.



main : Pour la production.

Configuration GitHub Actions

Créez un fichier .github/workflows/ci-cd.yml :

name: CI/CD Pipeline

on:
  push:
    branches:
      - dev
      - main
  pull_request:
    branches:
      - dev
      - master

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install Poetry
        run: pip install poetry
      - name: Install dependencies
        working-directory: ./server
        run: poetry install
      - name: Run Django tests
        working-directory: ./server
        run: poetry run python manage.py test
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'
      - name: Install Yarn
        run: npm install -g yarn
      - name: Install frontend dependencies
        working-directory: ./client
        run: yarn install
      - name: Build frontend
        working-directory: ./client
        run: yarn build

  deploy:
    needs: test
    if: github.ref == 'refs/heads/master'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to production
        run: echo "Déploiement sur le serveur de production (à configurer)"

Workflow





Push sur dev : Lance les tests unitaires pour le backend (Django) et le frontend (React).



Push sur master : Lance les tests et déploie sur un serveur de production (à configurer selon votre infrastructure).



Pull Requests : Vérifie les tests avant fusion dans dev ou master.

📝 Commandes utiles





Construire et lancer les conteneurs :

docker-compose up --build



Arrêter les conteneurs :

docker-compose down



Appliquer les migrations Django :

docker-compose exec web python manage.py migrate



Accéder à RabbitMQ Management :





URL : http://localhost:15672



Identifiants : guest / guest

🔐 Sécurité





Remplacez DJANGO_SECRET_KEY par une clé sécurisée.



Modifiez les identifiants par défaut de RabbitMQ et Grafana.



Configurez HTTPS pour Nginx en production (ajoutez un certificat SSL dans proxy/default.conf).

🌟 Prochaines étapes





Ajouter des tests unitaires pour Django (server/library/tests.py) et React (client/src/__tests__).



Implémenter des endpoints API REST pour la gestion des livres et emprunts.



Configurer des notifications par email via Celery pour les emprunts/retours.



Déployer sur un serveur cloud (AWS, GCP, ou autre) avec une pipeline CI/CD complète.

🤝 Contribuer





Forkez le dépôt.



Créez une branche (git checkout -b feature/nouvelle-fonctionnalite).



Commitez vos changements (git commit -m "Ajout de la fonctionnalité X").



Poussez sur la branche (git push origin feature/nouvelle-fonctionnalite).



Ouvrez une Pull Request vers dev.