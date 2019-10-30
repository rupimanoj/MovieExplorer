from flask import Flask, render_template, request
from flask_restful import  Api
from create_insert_queries import *
from flask_mysqldb import MySQL
from movies import Movies
from casts import Casts 
from studios import Studios
from theaters import Theaters
from shows import Shows
from users import Users
from ratings import Ratings
from flask_cors import CORS
from functions import Functions

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
api.add_resource(Movies, '/movies')
api.add_resource(Casts, '/casts')
api.add_resource(Studios, '/studios')
api.add_resource(Theaters, '/theaters')
api.add_resource(Shows, '/shows')
api.add_resource(Users, '/users')
api.add_resource(Ratings, '/ratings')
api.add_resource(Functions, '/functions')

#api.add_resource(Movie, '/movies/<movie_id>')
if __name__=='__main__':
	drop_all_tables();
	create_tables();
	app.run(debug=True)