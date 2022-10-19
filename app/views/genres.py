from flask_restx import Resource, Namespace
from app.models.genres import Genres, GenresSchema

genre_ns = Namespace('/genres')
genre_schema = GenresSchema()
genres_schema = GenresSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        try:
            genres = Genres.query.all()
            return genres_schema.dump(genres), 200
        except Exception as e:
            return e, 404


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        try:
            genre = Genres.query.get(gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return e, 404