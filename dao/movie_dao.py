from flask import request

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        movie = self.session.query(Movie).get(mid)
        if not movie:
            return "", 404
        return movie, 200

    def get_all(self):
        query = self.session.query(Movie).all()
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if year:
            query = query.filter(Movie.year == year)
        elif director_id:
            query = query.filter(Movie.director_id == director_id)
        elif genre_id:
            query = query.filter(Movie.genre_id == genre_id)
        return query, 200

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie, 201

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie, 204

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
