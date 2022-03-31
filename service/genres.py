from dao.genre import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_one(self, gid: int):
        return self.genre_dao.get_one(gid)

    def get_all(self):
        return self.genre_dao.get_all()
