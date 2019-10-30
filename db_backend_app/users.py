from flask_restful import reqparse
from flask import jsonify
from flask_restful import Resource
from create_insert_queries import *

list_parser = reqparse.RequestParser()
list_parser.add_argument('email', type=str, location='args')

show_parser = reqparse.RequestParser()
show_parser.add_argument('first_name')
show_parser.add_argument('last_name')
show_parser.add_argument('email')
show_parser.add_argument('fav_director')
show_parser.add_argument('fav_movie')


class Users(Resource):
	def get(self):
		filter_list = list_parser.parse_args()
		with app.app_context():
			get_users = get_all_users(filter_list)
		return get_users

	def post(self):
		args = show_parser.parse_args()
		insert_into_users(args)
		status_msg = "Succesfully inserted %s" %args["first_name"]
		return {"Status" : status_msg}
