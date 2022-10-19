from app.setup_db import db
from marshmallow import Schema, fields
from app.models.genres import GenresSchema
from app.models.directors import DirectorsSchema


class Movies(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre = db.relationship('Genres')
    director = db.relationship('Directors')


class MoviesSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre = fields.Pluck(field_name='name', nested=GenresSchema)
    director = fields.Pluck(field_name='name', nested=DirectorsSchema)

