from flask_restx import Resource, Namespace

from container import director_service
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        query = director_service.get_all()
        return directors_schema.dump(query), 200



@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        query = director_service.get_one(did)
        return director_schema.dump(query), 200
