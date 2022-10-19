from app.setup_db import db
from marshmallow import Schema, fields


class Directors(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class DirectorsSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
