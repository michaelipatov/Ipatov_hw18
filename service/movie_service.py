from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def post(self, data):
        return self.dao.create(data)

    def put(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def patch(self, data):
        mid = data.get("id")
        movie = self.dao.get_one(mid)

        if "title" in movie.title:
            movie.title = data.get("title")
        if "description" in movie.description:
            movie.description = data.get("description")
        if "trailer" in movie.trailer:
            movie.trailer = data.get("trailer")
        if "year" in movie.year:
            movie.year = data.get("year")
        if "rating" in movie.rating:
            movie.rating = data.get("rating")
        if "genre_id" in movie.genre_id:
            movie.genre_id = data.get("genre_id")
        if "director_id" in movie.director_id:
            movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.get_one(mid)
