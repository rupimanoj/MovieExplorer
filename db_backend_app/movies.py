from flask_restful import reqparse
from flask import jsonify
from flask_restful import Resource
from create_insert_queries import *



movies_parser = reqparse.RequestParser()
movies_parser.add_argument('movie_name')
movies_parser.add_argument('release_year', type = int)
movies_parser.add_argument('production_studio')
movies_parser.add_argument('director')
movies_parser.add_argument('producer')
movies_parser.add_argument('movie_category')
movies_parser.add_argument('language')
movies_parser.add_argument('cast_and_crew')

 
'''
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| movie_name        | varchar(255) | NO   | PRI | NULL    |       |
| release_year      | int(11)      | NO   | PRI | NULL    |       |
| production_studio | varchar(255) | YES  |     | NULL    |       |
| language          | varchar(255) | YES  |     | NULL    |       |
| movie_director    | varchar(255) | YES  |     | NULL    |       |
| movie_producer    | varchar(255) | YES  |     | NULL    |       |
| movie_length_mins | int(11)      | YES  |     | NULL    |       |
| budget            | int(11)      | YES  |     | NULL    |       |
| movie_category    | varchar(255) | YES  |     | NULL    |       |
'''
# class Movie(Resource):
#     def get(self, movie_id):
#         return {"particular movie get here" : "get here"}

#     def delete(self, movie_id):
#         return {"particular movie delete" : "delete here"}

#     def put(self, movie_id):
#         args = movies_parser.parse_args()
#         return {"particular movie" : "edit here"}

class Movies(Resource):
    def get(self):
        list_parser = reqparse.RequestParser()
        list_parser.add_argument('movie_name', type=str, location='args')
        list_parser.add_argument('release_year', type=int, location='args')
        filter_list = list_parser.parse_args()
        with app.app_context():
            movies_dict = get_all_movies(filter_list)
        return movies_dict

    def post(self):
        args = movies_parser.parse_args()
        insert_into_movies(args)
        insert_cast_in_movie_entries(args)
        status_msg = "Succesfully inserted %s" %args["movie_name"]
        return {"Status" : status_msg}