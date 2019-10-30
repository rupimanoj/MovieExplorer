from flask_mysqldb import MySQL
from flask import Flask
app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ROOTroot1'
app.config['MYSQL_DB'] = 'movie_db'


def construct_where_clause(filter_list):
	where_clause = ""
	for key, value in filter_list.items():
		q1 = ""
		if(value):
			if(type(value) == int):
				q1 = "%s = %d" %(key, value)
			else:
				q1 = "%s = '%s'" %(key, value)
			if(len(where_clause)):
				where_clause += " and "
			where_clause += q1
	if(len(where_clause)):
		where_clause = " where " + where_clause
	return where_clause

def execute_select_query(query):
	with app.app_context():
		cur = mysql.connection.cursor()
		cur.execute(query)
		result = cur.fetchall()
		mysql.connection.commit()
		cur.close()
	return result

def construct_dict_with_columns(columns_order, result):
	result_dict_list = []
	for row in result:
		row_dict = {}
		for a, b in zip(columns_order, row):
			row_dict[a] = b
		result_dict_list.append(row_dict)
	return result_dict_list

create_movies_table = "CREATE TABLE IF NOT EXISTS Movies (movie_id int NOT NULL AUTO_INCREMENT, \
										movie_name varchar(255), \
										release_year int, \
										production_studio varchar(255),\
										language varchar(255), \
										movie_director varchar(255), \
										movie_producer varchar(255), \
										movie_category varchar(255), \
										FOREIGN KEY (production_studio) REFERENCES Studios(studio_name),\
										PRIMARY KEY (movie_id, movie_name, release_year))"

def insert_into_movies(args):
	movie_name, release_year, production_studio = args['movie_name'], int(args['release_year']),\
	                                                   args['production_studio']
	language, director, producer =  args['language'], args['director'],args['producer'] 
	movie_category =  args['movie_category']                                                          
	query_values = "'%s',%d,'%s','%s','%s','%s','%s'" % (movie_name, release_year,production_studio,\
	                                              language, director, producer,\
	                                              movie_category)
	insert_movie_query = "INSERT INTO Movies(movie_name, release_year, production_studio, \
				language, movie_director, movie_producer, movie_category) values(%s)" % query_values
	with app.app_context():
		cur = mysql.connection.cursor()
		cur.execute(insert_movie_query)
		mysql.connection.commit()
		cur.close()

def get_all_movies(filter_list):
	where_clause = construct_where_clause(filter_list)
	select_movies_query = "Select * from Movies %s" %where_clause
	columns_order = ['movie_id', 'movie_name', 'release_year', 'production_studio'\
					'language', 'director', 'producer', 'movie_category']
	result = execute_select_query(select_movies_query)
	movies_list = construct_dict_with_columns(columns_order, result)
	return movies_list

create_cast_crew_in_movie_table = "CREATE TABLE IF NOT EXISTS CastAndMovies(\
											cast_name varchar(255),\
											cast_movie_id int NOT NULL AUTO_INCREMENT, \
											movie_id int,\
											FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),\
											PRIMARY KEY (cast_movie_id, movie_id, cast_name))"

def insert_cast_in_movie_entries(args):
	
	cast_crew = args['cast_and_crew'].split(',')
	movie_name = args['movie_name']
	release_year = args['release_year']
	query = "select * from Movies where movie_name = '%s' and release_year = %d" \
								%(movie_name, release_year)
	with app.app_context():
		cur = mysql.connection.cursor()
		cur.execute(query)
		result = cur.fetchall()
		if(len(result) != 1):
			return False
		movie_id = int(result[0][0])
		mysql.connection.commit()
		cur.close()

	with app.app_context():
		cur = mysql.connection.cursor()
		for cast_name in cast_crew:
			insert_query = "INSERT INTO CastAndMovies(movie_id, cast_name) \
									 values(%d, '%s')" %(movie_id, cast_name)
			cur.execute(insert_query)
		mysql.connection.commit()
		cur.close()

def get_all_cast_entries(filter_list):
	where_clause = construct_where_clause(filter_list)
	cast_query = "Select * from CastAndMovies %s" %where_clause
	columns_order = ['cast_name', 'cast_movie_id', 'movie_id']
	result =  execute_select_query(cast_query)
	cast_list = construct_dict_with_columns(columns_order, result)
	return cast_list

create_studios_table = "CREATE TABLE IF NOT EXISTS Studios(\
											studio_name varchar(255),\
											head_quarters varchar(255),\
											website varchar(255),\
											founder varchar(255),\
											PRIMARY KEY (studio_name))"

def insert_into_studios(args):
	studio_name = args['studio_name']
	head_quarters = args['head_quarters']
	website = args['website']
	founder = 	args['founder']
	with app.app_context():
		cur = mysql.connection.cursor()
		insert_query = "INSERT INTO Studios values('%s', '%s', '%s', '%s')" %(studio_name,\
													head_quarters, website, founder)
		cur.execute(insert_query)
		mysql.connection.commit()
		cur.close()

def get_all_studio_entries(filter_list):
	where_clause = construct_where_clause(filter_list)
	studios_query = "Select * from Studios %s" %where_clause
	columns_order = ['studio_name', 'head_quarters', 'website', 'founder']
	result =  execute_select_query(studios_query)
	studio_list = construct_dict_with_columns(columns_order, result)
	return studio_list

create_theaters_table = "CREATE TABLE IF NOT EXISTS Theaters(theater_name varchar(255), \
												city varchar(255), \
												screens_count int, \
												state varchar(255), \
												theater_id int NOT NULL AUTO_INCREMENT, \
												PRIMARY KEY (theater_id, theater_name, city))"

def get_all_theaters(filter_list):
	where_clause = construct_where_clause(filter_list)
	theaters_query = "Select * from Theaters %s" %where_clause
	columns_order = ['theater_name', 'city', 'screens_count',  'state', 'theater_id']
	result =  execute_select_query(theaters_query)
	theaters_list = construct_dict_with_columns(columns_order, result)
	return theaters_list

def insert_into_theaters(args):
	theater_name = args['theater_name']
	screens_count = int(args['screens_count'])
	city = args['city']
	state = args['state']
	with app.app_context():
		cur = mysql.connection.cursor()
		insert_query = "INSERT INTO Theaters (theater_name, city, screens_count, state) \
								values('%s', '%s',%d, '%s')" %(theater_name,\
								city, screens_count,state)
		cur.execute(insert_query)
		mysql.connection.commit()
		cur.close()

create_shows_table = "CREATE TABLE IF NOT EXISTS Shows(show_id int NOT NULL AUTO_INCREMENT, \
											screen_name varchar(255), \
											theater_id int ,\
											movie_id int, \
											show_date DATE, \
											show_start_time TIME, \
											show_end_time TIME, \
											FOREIGN KEY (theater_id) REFERENCES Theaters(theater_id),\
											FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),\
											PRIMARY KEY (show_id, screen_name, theater_id,\
											movie_id, show_date, show_start_time))"

def get_all_shows(filter_list):
	import json
	where_clause = construct_where_clause(filter_list)
	shows_query = "Select * from Shows %s" %where_clause
	columns_order = ['show_id', 'screen_name', 'theater_id', 'movie_name',
					'show_date','show_start_time','show_end_time']
	result =  execute_select_query(shows_query)
	shows_list = construct_dict_with_columns(columns_order, result)
	shows_list = json.dumps(shows_list,default=str)
	shows_list = json.loads(shows_list)
	return shows_list

def insert_into_shows(args):
	screen_name = args['screen_name']
	theater_name = args['theater_name']
	city = args['city']
	movie_name = args['movie_name']
	release_year = int(2019)
	query = "select * from Movies where movie_name = '%s' and release_year = %d" \
								%(movie_name, release_year)

	with app.app_context():
		cur = mysql.connection.cursor()
		cur.execute(query)
		result = cur.fetchall()
		if(len(result) != 1):
			return False
		movie_id = int(result[0][0])
		mysql.connection.commit()
		cur.close()

	show_date = args['show_date']
	show_start_time = args['show_start_time']
	show_end_time = args['show_end_time']
	query = "select * from Theaters where theater_name = '%s' and city = '%s'" \
								%(theater_name, city)
	with app.app_context():
		cur = mysql.connection.cursor()
		cur.execute(query)
		result = cur.fetchall()
		if(len(result) != 1):
			return False
		theater_id = int(result[0][4])
		mysql.connection.commit()
		cur.close()

	with app.app_context():
		cur = mysql.connection.cursor()
		insert_query = "INSERT INTO Shows (screen_name, theater_id, movie_id,\
					show_date,show_start_time,show_end_time) \
					values('%s', %d, %d, '%s', '%s','%s')" %(\
					screen_name, theater_id,\
					movie_id, show_date,show_start_time, show_end_time)
		cur.execute(insert_query)
		mysql.connection.commit()
		cur.close()

create_reviewers_table = "CREATE TABLE IF NOT EXISTS Users(first_name varchar(255),\
															  last_name varchar(255),\
															  email varchar(255), \
															  favorite_movie varchar(255), \
															  favorite_director varchar(255), \
															  PRIMARY KEY (email))"

def insert_into_users(args):
	first_name = args['first_name']
	last_name = args['last_name']
	email = args['email']
	fav_director = args['fav_director']
	fav_movie = args['fav_movie']
	with app.app_context():
		cur = mysql.connection.cursor()
		insert_query = "INSERT INTO Users values('%s','%s','%s','%s','%s')" %(first_name,\
											last_name,email,fav_movie,fav_director)
		cur.execute(insert_query)
		mysql.connection.commit()
		cur.close()

def get_all_users(filter_list):
	where_clause = construct_where_clause(filter_list)
	users_query = "Select * from Users %s" %where_clause
	columns_order = ['first_name', 'last_name', 'email', 'favorite_movie', 'favorite_director']
	result =  execute_select_query(users_query)
	users_list = construct_dict_with_columns(columns_order, result)
	return users_list

create_ratings_table = "CREATE TABLE IF NOT EXISTS Ratings (\
			movie_id int ,\
			user_email_id varchar(255),\
			rating int, \
			review_id int NOT NULL AUTO_INCREMENT, \
			FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),\
			FOREIGN KEY (user_email_id) REFERENCES Users(email), \
			PRIMARY KEY(review_id, movie_id, user_email_id))"

def get_all_ratings(filter_list):
	where_clause = construct_where_clause(filter_list)
	users_query = "Select * from Ratings %s" %where_clause
	columns_order = ['movie_id', 'user_email_id', 'rating', 'review_id']
	result =  execute_select_query(users_query)
	users_list = construct_dict_with_columns(columns_order, result)
	return users_list

def insert_into_ratings(args):
	movie_name = args['movie_name']
	release_year = int(args['release_year'])
	query = "select * from Movies where movie_name = '%s' and release_year = %d" \
								%(movie_name, release_year)
	with app.app_context():
		cur = mysql.connection.cursor()
		cur.execute(query)
		result = cur.fetchall()
		if(len(result) != 1):
			return False
		movie_id = int(result[0][0])
		mysql.connection.commit()
		cur.close()

	user_email_id = args['user_email_id']
	rating = int(args['rating'])
	with app.app_context():
		cur = mysql.connection.cursor()
		insert_query = "INSERT INTO Ratings (movie_id, user_email_id, rating) values(%d,'%s',%d)" %(movie_id,\
											user_email_id,rating)
		cur.execute(insert_query)
		mysql.connection.commit()
		cur.close()
	return True

def drop_all_tables():
	print("Dropping existing tables")
	with app.app_context():
		cur = mysql.connection.cursor()
		cur.execute("DROP TABLE IF EXISTS Ratings")
		cur.execute("DROP TABLE IF EXISTS Shows")
		cur.execute("DROP TABLE IF EXISTS CastAndMovies")
		cur.execute("DROP TABLE IF EXISTS Movies")
		cur.execute("DROP TABLE IF EXISTS Theaters")
		cur.execute("DROP TABLE IF EXISTS Screens")
		cur.execute("DROP TABLE IF EXISTS Studios")
		cur.execute("DROP TABLE IF EXISTS Users")
		mysql.connection.commit()
		cur.close()

def create_tables():
	print("creating tables")
	with app.app_context():
		cur = mysql.connection.cursor()
		tables_query_list = [create_studios_table,
							create_movies_table,
							create_cast_crew_in_movie_table,
							create_reviewers_table,
							create_ratings_table,  
							create_theaters_table,
							create_shows_table]
		for query in tables_query_list:
			#print('-----------------', query)
			cur.execute(query)
		mysql.connection.commit()
		cur.close()