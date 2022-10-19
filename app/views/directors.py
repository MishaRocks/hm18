from flask_restx import Resource, Namespace
from app.models.directors import Directors, DirectorsSchema

director_ns = Namespace('/directors')
director_schema = DirectorsSchema()
directors_schema = DirectorsSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        try:
            directors = Directors.query.all()
            return directors_schema.dumps(directors), 200
        except Exception as e:
            return e, 404


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get(self, gid):
        try:
            director = Directors.query.get(gid)
            return director_schema.dumps(director), 200
        except Exception as e:
            return e, 404
