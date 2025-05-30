import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
conn_params = {
    'dbname': os.getenv('POSTGRES_DB'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': '5432'
}
print(conn_params)
conn = psycopg2.connect(**conn_params)
print("Connexion réussie")
conn.close()