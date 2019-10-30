from flask_restful import reqparse
from flask import jsonify
from flask_restful import Resource
from create_insert_queries import *

list_parser = reqparse.RequestParser()
list_parser.add_argument('studio_name', type=str, location='args')

class Studios(Resource):
	def get(self):
		filter_list = list_parser.parse_args()
		with app.app_context():
			get_studios = get_all_studio_entries(filter_list)
		return get_studios

	def post(self):
		studio_parser = reqparse.RequestParser()
		studio_parser.add_argument('studio_name')
		studio_parser.add_argument('founder')
		studio_parser.add_argument('website')
		studio_parser.add_argument('head_quarters')
		args = studio_parser.parse_args()
		insert_into_studios(args)
		status_msg = "Succesfully inserted %s" %args["studio_name"]
		return {"Status" : status_msg}
