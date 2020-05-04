import markdown
import os
import shelve
import getMovieInformation.imdb_scrapper

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)


@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)



class MovieInformation(Resource):
    def get(self, moviename):
        try:
            movie_url_of_imdb=imdb_scrapper.find_movie_url(moviename)
            result=imdb_scrapper.get_movie_information(movie_url_of_imdb)
            return {'message': 'Movie found', 'data': result}, 200
        except:
            return {'message': 'Movie not found', 'data': {}}, 404

class MovieURL(Resource):
    def get(self, moviename):
        try:
            movie_url_of_imdb=imdb_scrapper.find_movie_url(moviename)
            return {'message': 'Movie found', 'data': movie_url_of_imdb}, 200
        except:
            return {'message': 'Movie not found', 'data': {}}, 404
   


# api.add_resource(DeviceList, '/devices')
api.add_resource(MovieInformation, '/movie/<string:moviename>')
api.add_resource(MovieURL, '/movieurl/<string:moviename>')

