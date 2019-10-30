from flask_restful import reqparse
from flask import jsonify
from flask_restful import Resource
from create_insert_queries import *

list_parser = reqparse.RequestParser()
list_parser.add_argument('theater_name', type=str, location='args')
list_parser.add_argument('city', type=str, location='args')

theater_parser = reqparse.RequestParser()
theater_parser.add_argument('theater_name')
theater_parser.add_argument('city')
theater_parser.add_argument('screens_count')
theater_parser.add_argument('state')

class Theaters(Resource):
	def get(self):
		filter_list = list_parser.parse_args()
		with app.app_context():
			get_theaters = get_all_theaters(filter_list)
		return get_theaters

	def post(self):
		args = theater_parser.parse_args()
		insert_into_theaters(args)
		status_msg = "Succesfully inserted %s" %args["theater_name"]
		return {"Status" : status_msg}
