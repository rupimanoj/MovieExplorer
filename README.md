# MovieExplorer

## Queries files
  * For creation of tables and insert queries - db_backend_app/create_insert_queries.py
  * For queries to support high level cases in UI - db_backend_app/function_queries.py
## Data
 * All the data related scripts and extracted data in - db_backend_app/data folder
 
## UI
  * ReactJS based code in Database-UI folder.
 
## Setup instructions:
# Backend setup.
* To support all the third party packages, python anaconda environment is used.
 [Install Anaconda python 3.7] https://www.anaconda.com/distribution/#download-section. 
* conda create -n db_setup python=3
* conda activate db_setup
* conda install -c anaconda flask
* conda install -c conda-forge/label/gcc7 flask-restful
* ~/anaconda3/envs/db_setup/bin/pip install Flask-MySQLdb
#  To fill DB with mock data.
* Create MYSQL DB with username 'root', password 'ROOTroot1' and db name movie_db
* Start application with python app.py. Make sure conda environment db_setup is activated.
* conda install ipykernel
* python -m ipykernel install --user --name db_setup
* Start jupyter notebook
* Run db_filler notebook from data folder. As there are foreign keys dependencies, Studios table need to get filled before Movies table. Make sure correct order is followed while filling tables. In existing notebook cells should be executed in the order of 1, 3, 2, 4, 5, 6, 7.
* Keep backend server in running state so that front end requests are also processed.

# Frontend setup.
* Install npm to run reactjs server.
* export HOST=localhost.
* Install required packages.
* npm install react-jsonschema-form --save.
* npm install bootstrap.
* npm install react-table.
* Move to UI folder Database-UI and run command npm start.
* This should bringup local website in default web browser.
* Submit DB requests using Frontend UI.

