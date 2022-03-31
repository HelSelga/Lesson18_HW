from dao.models.directors import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did: int):
        return self.session.query(Director).filter(Director.id == did).first()

    def get_all(self):
        return self.session.query(Director).all()
