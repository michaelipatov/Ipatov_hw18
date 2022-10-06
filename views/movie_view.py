from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema


movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        query = movie_service.get_all()
        return movies_schema.dump(query), 200

    def create(self):
        data = request.json
        movie_service.post(data)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        query = movie_service.get_one(mid)
        return movie_schema.dump(query), 200

    def put(self, mid: int):
        data = request.json
        data["id"] = mid

        movie_service.put(data)
        return "", 204

    def patch(self, mid: int):
        data = request.json
        data["id"] = mid

        movie_service.patch(data)
        return "", 204

    def delete(self, mid: int):
        movie_service.delete(mid)
        return "", 204
