from flask_restful import reqparse
from flask import jsonify
from flask_restful import Resource
from create_insert_queries import *

list_parser = reqparse.RequestParser()
list_parser.add_argument('user_email_id', type=str, location='args')

show_parser = reqparse.RequestParser()
show_parser.add_argument('movie_name')
show_parser.add_argument('release_year')
show_parser.add_argument('user_email_id')
show_parser.add_argument('rating')


class Ratings(Resource):
	def get(self):
		filter_list = list_parser.parse_args()
		with app.app_context():
			get_ratings = get_all_ratings(filter_list)
		return get_ratings

	def post(self):
		args = show_parser.parse_args()
		insert_into_ratings(args)
		status_msg = "Succesfully inserted %s stars" %args["rating"]
		return {"Status" : status_msg}
