from flask_restful import reqparse
from flask import jsonify
from flask_restful import Resource
from create_insert_queries import *

'''
mysql> describe CastAndMovies;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| movie_name   | varchar(255) | NO   | PRI | NULL    |       |
| release_year | int(11)      | NO   | PRI | NULL    |       |
| cast_name    | varchar(255) | NO   | PRI | NULL    |       |
+--------------+--------------+------+-----+---------+-------+

'''

list_parser = reqparse.RequestParser()
list_parser.add_argument('movie_name', type=str, location='args')
list_parser.add_argument('release_year', type=int, location='args')
list_parser.add_argument('cast_name', type=str, location='args')

class Casts(Resource):
	def get(self):
		filter_list = list_parser.parse_args()
		with app.app_context():
			get_cast_entries = get_all_cast_entries(filter_list)
		return get_cast_entries

	def post(self):
		args = studio_parser.parse_args()
		insert_studio(args)
		status_msg = "Succesfully inserted %s" %args["studio_name"]
		return {"Status" : status_msg}