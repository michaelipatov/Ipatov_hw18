from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        director = self.session.query(Director).get(did)
        if not director:
            return "", 404
        return director, 200

    def get_all(self):
        return self.session.query(Director).all(), 200
