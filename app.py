from flask import Flask
from flask_restx import Api

from config import Config

from setup_db import db

from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns


def create_app(config_object):
    """
    Функция создания основного объекта app
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)

    return app


def register_extensions(app: Flask):
    """
    Функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, и т.д.)
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
