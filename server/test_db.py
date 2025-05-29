import psycopg2

try:
    conn = psycopg2.connect(
        dbname='devops_db',
        user='devops_user',
        password='devops_pass',
        host='localhost'  # ou 'db' si en Docker
    )
    print("✅ Connexion à PostgreSQL réussie!")
    conn.close()
except Exception as e:
    print(f"❌ Erreur de connexion: {e}")