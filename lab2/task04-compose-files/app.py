from flask import Flask, render_template_string
import psycopg2

app = Flask(__name__)


@app.route("/")
def index():
    conn = psycopg2.connect(
        # ВПИШИТЕ имя сервиса базы данных из docker-compose.yml:
        host="db",
        port="5432",
        database="mydb",
        user="postgres",
        password="mysecretpassword",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users;")
    users = cursor.fetchall()
    conn.close()
    return render_template_string(
        "<h1>Users</h1><ul>{% for user in users %}<li>{{ user[0] }}</li>{% endfor %}</ul>",
        users=users,
    )


if __name__ == "__main__":
    # chunks = []
    # import time
    # while True:
    #     chunks.append(bytearray(10 * 1024 * 1024))
    #     chunks[-1][:] = b"x" * len(chunks[-1])
    #     time.sleep(0.1)
    app.run(host="0.0.0.0", port=5001)
