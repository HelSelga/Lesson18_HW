# Сервис-контейнер - файл для создания DAO и сервисов,
# чтобы импортировать их везде

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from service.directors import DirectorService
from service.genres import GenreService
from dao.movie import MovieDAO
from service.movies import MovieService
from setup_db import db


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
