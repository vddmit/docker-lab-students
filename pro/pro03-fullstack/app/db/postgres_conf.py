import os

from psycopg2.pool import ThreadedConnectionPool
from dotenv import load_dotenv


load_dotenv()

pool = ThreadedConnectionPool(
    minconn=1,
    maxconn=10,
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DATABASE"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)

def get_connection():
    return pool.getconn()

def release_connection(conn):
    pool.putconn(conn)