
from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db

from app.views.genres import genre_ns
from app.views.directors import director_ns
from app.views.movies import movie_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
