import React, { Component } from 'react';
import {render} from "react-dom";
import Form from "react-jsonschema-form";
import axios from 'axios';

const apiEndPoint = "http://127.0.0.1:5000/shows";

const invokeAjaxCall = async (form) => {
    console.log(form.formData);
    const {data: post} = await axios.post(apiEndPoint, form.formData);
}

const schema = require("../json_forms/shows.json");
class Shows extends Component {
    render(){
        return(<Form schema = {schema}
            onSubmit = {invokeAjaxCall}/>);
    };
}
 
export default Shows;