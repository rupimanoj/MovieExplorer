from flask_restful import reqparse
from flask import jsonify
from flask_restful import Resource
from create_insert_queries import *
from function_queries import *
import json



args_parser = reqparse.RequestParser()
args_parser.add_argument('function_type', type=str, location='args')

class Functions(Resource):
	def get(self):
		functions_parser = reqparse.RequestParser()
		functions_parser.add_argument('movie_name', type=str)
		functions_parser.add_argument('release_year', type=int)
		functions_parser.add_argument('cast_name', type=str)
		functions_parser.add_argument('director_name', type=str)
		functions_parser.add_argument('theater_name', type=str)
		functions_parser.add_argument('city', type=str)
		functions_parser.add_argument('date', type=str)
		functions_parser.add_argument('email', type=str)
		params_list = functions_parser.parse_args()
		args_list = args_parser.parse_args()
		print("----------------------",params_list, args_list)
		result = handle_functions(params_list, args_list['function_type'])
		return result

	def post(self):
		functions_parser = reqparse.RequestParser()
		functions_parser.add_argument('movie_name', type=str)
		functions_parser.add_argument('release_year', type=int)
		functions_parser.add_argument('cast_name', type=str)
		functions_parser.add_argument('director_name', type=str)
		functions_parser.add_argument('theater_name', type=str)
		functions_parser.add_argument('city', type=str)
		functions_parser.add_argument('date', type=str)
		functions_parser.add_argument('email', type=str)
		params_list = functions_parser.parse_args()
		args_list = args_parser.parse_args()
		print("----------------------",params_list, args_list)
		result = handle_functions(params_list, args_list['function_type'])
		return result