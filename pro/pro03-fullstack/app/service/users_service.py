
from db.postgres_conf import get_connection, release_connection



def get_users():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
                return users
    finally:
        release_connection(conn)
