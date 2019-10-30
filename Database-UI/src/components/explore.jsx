import React, { Component } from 'react';
import {render} from "react-dom";
import Form from "react-jsonschema-form";
import axios from 'axios';
import ReactTable from 'react-table'
import 'react-table/react-table.css'


const user_schema 	= require("../json_forms/user_schema.json");
const movie_schema 	= require("../json_forms/movie_schema.json");
const cast_schema 	= require("../json_forms/cast_schema.json");
const director_schema = require("../json_forms/director_schema.json");
const director_cast_schema = require("../json_forms/director_cast_schema.json");
const theater_shows_schema 	= require("../json_forms/theater_shows_schema.json");
const movies_shows_schema 	= require("../json_forms/movies_shows_schema.json");


const user_columns = [
	{
		Header: 'First Name',
		accessor: 'first_name' 
	}, 
	{
		Header: 'Last Name',
		accessor: 'last_name'
	},
	{
		Header: 'EMail id',
		accessor: 'email' 
	}, 
	{
		Header: 'Favorite movie',
		accessor: 'favorite_movie'
	},
	{
		Header: 'Favorite director',
		accessor: 'favorite_director' 
	},
	{
		Header: 'Average rating',
		accessor: 'avg_rating' 
	}

];

const movie_columns = [
	{
		Header: 'Movie Name',
		accessor: 'movie_name' 
	}, 
	{
		Header: 'Release year',
		accessor: 'release_year'
	},
	{
		Header: 'Director',
		accessor: 'movie_director' 
	}, 
	{
		Header: 'Producer',
		accessor: 'movie_producer'
	},
	{
		Header: 'Studio',
		accessor: 'production_studio' 
	},
	{
		Header: 'Average rating',
		accessor: 'avg_rating' 
	}

];

const show_columns = [
	{
		Header: 'Movie Name',
		accessor: 'movie_name' 
	},
	{
		Header: 'Theater name',
		accessor: 'theater_name' 
	}, 
	{
		Header: 'City',
		accessor: 'city'
	},
	{
		Header: 'Screen',
		accessor: 'screen_name'
	},
	{
		Header: 'Date',
		accessor: 'show_date' 
	},
	{
		Header: 'start time',
		accessor: 'show_start_time' 
	},
	{
		Header: 'end time',
		accessor: 'show_end_time' 
	},


];

class Explore extends Component {
	
	constructor(props)
	{
		super(props);
		this.state = {user_specific_information:[],
					movie_specific_information:[],
					director_movies_information:[],
					cast_movies_information:[],
					director_cast_movies_information:[],
					shows_movies_information:[],
					theater_movies_information:[]};
	}

	invoke_user_specific_call = async (form) => {
		const apiEndPoint = "http://127.0.0.1:5000/functions?function_type=specific_user";
	    const {data: post} = await axios.post(apiEndPoint, form.formData);
	    this.setState({user_specific_information: post});
	    console.log(post);
	}

	invoke_movie_specific_call = async (form) => {
		const apiEndPoint = "http://127.0.0.1:5000/functions?function_type=specific_movie";
	    const {data: post} = await axios.post(apiEndPoint, form.formData);
	    this.setState({movie_specific_information: post});

	}

	invoke_cast_specific_call = async (form) => {
		const apiEndPoint = "http://127.0.0.1:5000/functions?function_type=movies_by_cast";
	    const {data: post} = await axios.post(apiEndPoint, form.formData);
	    this.setState({cast_movies_information: post});
	}

	invoke_director_specific_call = async (form) => {
		const apiEndPoint = "http://127.0.0.1:5000/functions?function_type=movies_by_director";
	    const {data: post} = await axios.post(apiEndPoint, form.formData);
	    this.setState({director_movies_information: post});
	}

	invoke_director_cast_specific_call = async (form) => {
		const apiEndPoint = "http://127.0.0.1:5000/functions?function_type=movies_by_cast_and_director";
	    const {data: post} = await axios.post(apiEndPoint, form.formData);
	    this.setState({director_cast_movies_information: post});
	}

	invoke_theater_shows_specific_call = async (form) => {
		const apiEndPoint = "http://127.0.0.1:5000/functions?function_type=shows_in_theater";
	    const {data: post} = await axios.post(apiEndPoint, form.formData);
	    this.setState({theater_movies_information: post});
	}

	invoke_movies_shows_specific_call = async (form) => {
		const apiEndPoint = "http://127.0.0.1:5000/functions?function_type=shows_for_movie";
	    const {data: post} = await axios.post(apiEndPoint, form.formData);
	    console.log(post);
	    this.setState({shows_movies_information: post});
	}

    render(){
        return(
        <div className="container">
	        <div className="container">
	        	<h1>{this.state.counter}</h1>
	        	<h3 class="text-white bg-dark">Get User Details</h3>
	        	<Form schema = {user_schema} onSubmit = {this.invoke_user_specific_call}/>
	        	<ReactTable data={this.state.user_specific_information} columns={user_columns} minRows ={0} showPagination = {false}/>
	        	<br/>
	        </div>
	        <div className="container">
	        	<h3 class="text-white bg-dark">Get Movie Details</h3>
	        	<Form schema = {movie_schema} onSubmit = {this.invoke_movie_specific_call}/>
	        	<ReactTable data={this.state.movie_specific_information} columns={movie_columns} minRows ={0} showPagination = {false}/>
	        	<br/>
	        </div>
	        <div className="container">
	        	<h3 class="text-white bg-dark">Get Director Movies</h3>
	        	<Form schema = {director_schema} onSubmit = {this.invoke_director_specific_call}/>
	        	<ReactTable data={this.state.director_movies_information} columns={movie_columns} minRows ={0} showPagination = {false}/>
	        	<br/>
	        </div>
	        <div className="container">
	        	<h3 class="text-white bg-dark">Get Cast Candidate Movies</h3>
	        	<Form schema = {cast_schema} onSubmit = {this.invoke_cast_specific_call}/>
	        	<ReactTable data={this.state.cast_movies_information} columns={movie_columns} minRows ={0} showPagination = {false}/>
	        	<br/>
	        </div>
	        <div className="container">
	        	<h3 class="text-white bg-dark">Get Director & Cast Movies</h3>
	        	<Form schema = {director_cast_schema} onSubmit = {this.invoke_director_cast_specific_call}/>
	        	<ReactTable data={this.state.director_cast_movies_information} columns={movie_columns} minRows ={0} showPagination = {false}/>
	        	<br/>
	        </div>
	        <div className="container">
	        	<h3 class="text-white bg-dark">Get shows in a theater</h3>
	        	<Form schema = {theater_shows_schema} onSubmit = {this.invoke_theater_shows_specific_call}/>
	        	<ReactTable data={this.state.theater_movies_information} columns={show_columns} minRows ={0} showPagination = {false}/>
	        	<br/>
	        	<br/>
	        </div>
	        <div className="container">
	        	<h3 class="text-white bg-dark">Get Shows for a movie</h3>
	        	<Form schema = {movies_shows_schema} onSubmit = {this.invoke_movies_shows_specific_call}/>
	        	<ReactTable data={this.state.shows_movies_information} columns={show_columns} minRows ={0} showPagination = {false}/>
	        	<br/>
	        </div>
        </div>
        );
    };
}
 
export default Explore;