from flask import request
from flask_restx import Resource, Namespace
from dao.models.movies import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies_query = movie_service.get_all()
        return movies_schema.dump(movies_query), 200

    def post(self):
        req_json = request.json
        new_movie = movie_service.create(req_json)
        return None, 201, {"location": f"/movies/{new_movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, mid: int):
        req_json = request.json
        req_json["id"] = mid
        updated_movie = movie_service.update(req_json)

        if updated_movie != 1:
            return None, 400

        return None, 204

    def delete(self, mid: int):
        movie = movie_service.delete(mid)
        if movie != 1:
            return None, 400

        return None