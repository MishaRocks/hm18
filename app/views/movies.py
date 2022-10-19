from flask_restx import Resource, Namespace
from app.models.movies import Movies, MoviesSchema
from flask import request
from app.setup_db import db

movie_ns = Namespace('/movies')
movie_schema = MoviesSchema()
movies_schema = MoviesSchema(many=True)


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        all_movies = Movies.query.all()
        result = movies_schema.dump(all_movies)

        director_id = request.args.get('director_id')
        if director_id:
            movies = Movies.query.filter(Movies.director_id == director_id)
            result = movies_schema.dump(movies)

        genre_id = request.args.get('genre_id')
        if genre_id:
            movies = Movies.query.filter(Movies.genre_id == genre_id)
            result = movies_schema.dump(movies)

        year = request.args.get('year')
        if year:
            m_year = Movies.query.filter(Movies.year == year)
            result = movies_schema.dump(m_year)

        return result

    def post(self):
        data = request.json
        try:
            db.session.add(Movies(**data))
            db.session.commit()
            return "Всё норм прошло", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = Movies.query.get(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        try:
            db.session.query(Movies).filter(Movies.id == mid).update(data)
            db.session.commit()
            return "Данные обновлены", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return e, 200

    def delete(self, mid):
        try:
            db.session.query(Movies).filter(Movies.id == mid).delete()
            db.session.commit()
            return "Данные удалены", 201
        except Exception as e:
            return e, 403
