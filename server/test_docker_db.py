import psycopg2
import os

# Configuration from your .env file
DB_CONFIG = {
    'dbname': 'devops_db',
    'user': 'devops_user',
    'password': 'devops_pass',
    'host': 'localhost',
    'port': 5432
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print("✅ Connexion à PostgreSQL réussie!")
    print("Version PostgreSQL:", cursor.fetchone()[0])
    conn.close()
except Exception as e:
    print(f"❌ Erreur de connexion: {e}")
    print("Vérifiez que:")
    print("1. Le conteneur PostgreSQL est en cours d'exécution")
    print("2. Le port 5432 est exposé dans docker-compose.yml")
    print("3. Les identifiants dans le fichier .env sont corrects")