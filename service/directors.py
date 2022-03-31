from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_one(self, did: int):
        return self.director_dao.get_one(did)

    def get_all(self):
        return self.director_dao.get_all()
