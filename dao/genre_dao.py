from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        genre = self.session.query(Genre).get(gid)
        if not genre:
            return "", 404
        return genre, 200

    def get_all(self):
        return self.session.query(Genre).all(), 200
