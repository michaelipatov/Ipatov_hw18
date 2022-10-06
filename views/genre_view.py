from flask_restx import Resource, Namespace

from container import genre_service
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        query = genre_service.get_all()
        return genres_schema.dump(query), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        query = genre_service.get_one(gid)
        return genre_schema.dump(query), 200
