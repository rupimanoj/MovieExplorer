from flask_restful import reqparse
from flask import jsonify
from flask_restful import Resource
from create_insert_queries import *

list_parser = reqparse.RequestParser()
list_parser.add_argument('theater_name', type=str, location='args')
list_parser.add_argument('city', type=str, location='args')
list_parser.add_argument('show_date', type=str, location='args')

show_parser = reqparse.RequestParser()
show_parser.add_argument('screen_name')
show_parser.add_argument('theater_name')
show_parser.add_argument('city')
show_parser.add_argument('movie_name')
show_parser.add_argument('show_start_time')
show_parser.add_argument('show_end_time')
show_parser.add_argument('show_date')


class Shows(Resource):
	def get(self):
		filter_list = list_parser.parse_args()
		with app.app_context():
			get_shows = get_all_shows(filter_list)
		return get_shows

	def post(self):
		args = show_parser.parse_args()
		insert_into_shows(args)
		status_msg = "Succesfully inserted %s" %args["theater_name"]
		return {"Status" : status_msg}
