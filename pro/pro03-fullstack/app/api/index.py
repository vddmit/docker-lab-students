from flask import Blueprint, render_template_string
from service.users_service import get_users
from db.redis_conf import client

index_router = Blueprint("users", __name__)


@index_router.get("/")
def index():
    visits = client.incr("index_page_visits")

    return render_template_string(
        """
        <h1>Users</h1>
        <p>Количество посещений: {{ visits }}</p>
        <ul>
            {% for user in users %}
                <li>ID: {{ user[0] }}, Name: {{ user[1] }}</li>
            {% endfor %}
        </ul>
        """,
        users=get_users(),
        visits=visits,
    )
