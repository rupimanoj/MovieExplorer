from flask_mysqldb import MySQL
from flask import Flask
from decimal import Decimal
import datetime

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ROOTroot1'
app.config['MYSQL_DB'] = 'movie_db'

def execute_select_query(query):
	with app.app_context():
		cur = mysql.connection.cursor()
		cur.execute(query)
		result = cur.fetchall()
		columns = field_names = [i[0] for i in cur.description]
		mysql.connection.commit()
		cur.close()
	return result, columns

def construct_dict_with_columns(columns_order, result):
	result_dict_list = []
	for row in result:
		row_dict = {}
		for a, b in zip(columns_order, row):
			if type(b) is Decimal:
				row_dict[a] = float(b)
			else:
				row_dict[a] = str(b)
		result_dict_list.append(row_dict)
	return result_dict_list

def handle_specific_user_query(args):
	email = args['email']
	select_user_query = "select Users.*, avg_rating from \
						Users INNER JOIN (select user_email_id, avg(rating) as avg_rating from \
						Ratings group by user_email_id) as agg_rating on Users.email = '%s' \
						and Users.email = agg_rating.user_email_id" % email
	result,columns = execute_select_query(select_user_query)
	output = construct_dict_with_columns(columns, result)
	return output

def handle_specific_movie_query(args):
	release_year = args['release_year']
	movie_name = args['movie_name']
	select_movie_query = "select Movies.*, avg_rating from Movies \
							INNER JOIN (select movie_id, avg(rating) as avg_rating from Ratings \
							group by movie_id) as agg_rating on Movies.movie_name = '%s' and \
							Movies.release_year = %d and Movies.movie_id = agg_rating.movie_id" \
							% (movie_name, release_year)
	result,columns = execute_select_query(select_movie_query)
	output = construct_dict_with_columns(columns, result)
	return output

def handle_specific_movies_by_director_query(args):
	director_name = args['director_name']
	select_movies_query = "select Movies.*, avg_rating from Movies \
	 						INNER JOIN (select movie_id, avg(rating) as avg_rating from \
	 						Ratings group by movie_id) as agg_rating on Movies.movie_director = '%s' \
	 						and Movies.movie_id = agg_rating.movie_id" % director_name
	result,columns = execute_select_query(select_movies_query)
	output = construct_dict_with_columns(columns, result)
	return output

def handle_specific_movies_by_cast_query(args):
	cast_name = args['cast_name']
	select_movies_query = "Select CastMovies.*, agg_rating.avg_rating from \
							(Select Movies.* from Movies \
							 Inner Join CastAndMovies where cast_name = '%s' and \
							 CastAndMovies.movie_id = Movies.movie_id) as CastMovies \
							  inner join (Select avg(rating) as avg_rating,\
						  	  movie_id from Ratings group by movie_id) as agg_rating on \
						  	  agg_rating.movie_id = CastMovies.movie_id" % cast_name
	result,columns = execute_select_query(select_movies_query)
	output = construct_dict_with_columns(columns, result)
	return output

def handle_movies_by_cast_and_director_query(args):
	cast_name = args['cast_name']
	director_name = args['director_name']
	select_movies_query = "Select CastMovies.*, agg_rating.avg_rating from \
						(Select Movies.* from Movies Inner Join CastAndMovies \
						where cast_name = '%s' and movie_director = '%s'\
	 					and CastAndMovies.movie_id = Movies.movie_id) as CastMovies \
	 					inner join (Select avg(rating) as avg_rating,movie_id from Ratings \
	 					group by movie_id) as agg_rating on \
	 					agg_rating.movie_id = CastMovies.movie_id"%(cast_name, director_name)
	result,columns = execute_select_query(select_movies_query)
	output = construct_dict_with_columns(columns, result)
	return output

def handle_shows_in_theater_query(args):
	theater_name = args['theater_name']
	city		= args['city']
	date		= args['date']
	select_movies_query = "Select Movies.movie_name, show_theaters.* from Movies inner join \
					(Select Shows.*, Theaters.theater_name, Theaters.city from Theaters \
					join Shows on Theaters.theater_id = Shows.theater_id and \
					Shows.show_date = '%s' and Theaters.theater_name = '%s' \
					and Theaters.city='%s') as show_theaters on \
					show_theaters.movie_id = Movies.movie_id;"%(date, theater_name, city)
	result,columns = execute_select_query(select_movies_query)
	output = construct_dict_with_columns(columns, result)
	return output

def handle_shows_for_movie_query(args):
	movie_name = args['movie_name']
	release_year = args['release_year']
	city		= args['city']
	date		= args['date']
	select_movies_query = "Select Movies.movie_name, show_theaters.* from Movies join \
						(Select Shows.*, Theaters.theater_name, Theaters.city from Theaters join \
	 					Shows on Shows.theater_id = Theaters.theater_id and Theaters.city='%s' \
	 					and Shows.show_date = '%s') as show_theaters \
						on show_theaters.movie_id = Movies.movie_id and movie_name = '%s' \
						and release_year = %d;"%(city, date, movie_name, release_year)
	result,columns = execute_select_query(select_movies_query)
	output = construct_dict_with_columns(columns, result)
	return output

def handle_functions(args, function_type):
	if function_type == "specific_user":
		return handle_specific_user_query(args)
	elif function_type == "specific_movie":
		return handle_specific_movie_query(args)
	elif function_type == "movies_by_director":
		return handle_specific_movies_by_director_query(args)
	elif function_type == "movies_by_cast":
		return handle_specific_movies_by_cast_query(args)
	elif function_type == "movies_by_cast_and_director":
		return handle_movies_by_cast_and_director_query(args)
	elif function_type == "shows_in_theater":
		return handle_shows_in_theater_query(args)
	elif function_type == "shows_for_movie":
		return handle_shows_for_movie_query(args)
	return
