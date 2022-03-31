from flask import request

from dao.models.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid: int):
        return self.session.query(Movie).filter(Movie.id == mid).first()

    def get_all(self):
        movie_list = self.session.query(Movie)
        query = request.args

        if "director_id" in query:
            movie_list = movie_list.filter(Movie.director_id == query.get("director_id"))
        if "genre_id" in query:
            movie_list = movie_list.filter(Movie.genre_id == query.get("genre_id"))
        if "year" in query:
            movie_list = movie_list.filter(Movie.year == query.get("year"))

        return movie_list.all()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid: int):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
