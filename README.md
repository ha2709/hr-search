# hr-search

## Activate enviroment  

`source env/bin/activate`

## project name is hr_app

## rename or copy .env.example to .env in each service

## To run API, `uvicorn api.main:app --reload --port 8001`

## To run Django : `python3 hr_app/manage.py runserver`

## To run migration : `python3 hr_app/manage.py migrate`

## To login in terminal run 

`python3 hr_app/manage.py createsuperuser`

then set your user name and pass. 

acess to browser `http://localhost:8000/admin/`

login with your username (admin) and password (1234). Now you can navigate to 

`http://localhost:8000/api/`

`python3 hr_app/manage.py makemigrations`

## on browser : `http://localhost:8000/api/`

Access the OpenAPI Docs: Visit http://localhost:8001/docs or http://localhost:8001/redoc

## To generate requirements.txt 

`pip freeze > requirements.txt`

` chmod -R 777 /var/run/docker.sock`

## in hr-search/hr-app: 

`docker build -t hr-django-app .`

`docker run -p 8000:8000 hr-django-app`

## in hr-search/api

`docker build -t fast-hr-app .`


`docker run -p 8001:8001 fast-hr-app`

The services folder is used for interact with DB
the utils forlder is for common functions used in programs
The routers contains all the route
the Models folder contains all the model. I use ORM for some benefits: using object rather than write query, code easier to read and maintain, easy to switch between databases, automatic create tables, avoid writting complex query, data is validated.  In case of millions users in DB. it help to reduce redundancy for the position, location, status... (we only load the id instead of loading the name of it - position, location, department ) in the table Employee. It helps better retrieve data.  
Django will read from .env and send them to the template via context: such as API key, API key name, API url ... 

For the search array of status, I will combine result for each status. 

To help scale up, it will read the server's API from .env. 