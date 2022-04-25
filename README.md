# "YaMDb"

![YAMDB workflow status](https://github.com/SokolovskiR/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

## Description
This is a RESTful API for "YaMDb", a rating service for artworks like movies, books or songs.
## Technology
* Python 3.7
* Django 2.2.16
* Django REST framework 3.12.4
## How to run the project in dev-mode
- clone this repository to your local machine
```
git clone https://github.com/SokolovskiR/api_yamdb
``` 
- create a virtual environment
```
python3 m -venv venv
``` 
- activate virtual environment
```
source venv/bin/activate
``` 
- install dependencies in requirements.txt
```
pip install -r requirements.txt
``` 
- inside the folder with manage.py file execute the following command for migrations:

```
python3 manage.py migrate
```
- inside the same folder execute this command to create a superuser:
```
python3 manage.py createsuperuser
```
- inside the same folder execute this command to start the development server:
```
python3 manage.py runserver
```

## REST API available endpoints

After you started the development server, go to */api/v1/redoc/* URL where you can find the API documentation with available endpoints.


## Public Deployment

You can check the deployed project by visiting this public site: http://romka-yatube.hopto.org/api/v1/

API Documentation is available under: http://romka-yatube.hopto.org/redoc/


### Authors
RomanS, AlexanderK, RomanY
