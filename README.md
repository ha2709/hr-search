# hr-search

## Activate enviroment  

`source env/bin/activate`

## project name is hr_app

## To run API, `uvicorn api.main:app --reload --port 8001`

## To run Django : `python3 hr_app/manage.py runserver`

## To run migration : `python3 hr_app/manage.py migrate`

Access the OpenAPI Docs: Visit http://localhost:8000/docs or http://localhost:8000/redoc

## To generate requirements.txt 

`pip freeze > requirements.txt`

` chmod -R 777 /var/run/docker.sock`

## in hr-search/hr-app: 

`docker build -t hr-django-app .`

`docker run -p 8000:8000 hr-django-app`

## in hr-search/api

`docker build -t fast-hr-app .`



`docker run -p 8001:8001`