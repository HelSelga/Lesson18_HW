from dao.models.genres import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid: int):
        return self.session.query(Genre).filter(Genre.id == gid).first()

    def get_all(self):
        return self.session.query(Genre).all()
