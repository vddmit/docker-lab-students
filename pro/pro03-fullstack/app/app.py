from flask import Flask
from api.index import index_router

app = Flask(__name__)
app.register_blueprint(index_router)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
