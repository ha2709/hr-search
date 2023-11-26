# hr-search

## Activate Enviroment  

To activate the virtual environment, run:

`source env/bin/activate`

## Project Name  

The project name is `hr_search` .

## Running the Docker Compose Setup

To enable Docker on VS Code, you may need to execute the following commands:

```
sudo su
chmod -R 777 /var/run/docker.sock
 
```

To run the Docker Compose setup and build the containers, execute the following command in your terminal:

```
cd hr_search
docker-compose up --build
```

To run docker next time:

`docker-compose up`

## Set Up Environment Variables

rename or copy .env.example to .env in each service.

## Run API

To run API, use the following command:

 `uvicorn api.main:app --reload --port 8001`

## To run Test API :

```
git checkout tests
cd api
pytest
```

## Run Django

To run Django : `python3 hr_app/manage.py runserver`

## Run Migration

To run migrations, use : `python3 hr_app/manage.py migrate`

## Create Superuser

To create a superuser, run:

`python3 hr_app/manage.py createsuperuser`

Follow the prompts to set your username and password.

Access the Django admin panel at: `http://localhost:8000/admin/` .

Navigate to `http://localhost:8000/api/` for API functionality.

Access the OpenAPI Docs: Visit http://localhost:8001/docs or http://localhost:8001/redoc

## Generate requirements.txt

To generate requirements.txt, run:

`pip freeze > requirements.txt`

## Docker Build for Django



List processes running on port 8000:

`lsof -i : 8000`

Kill the specified process:

`kill -9 <pid>`

## Stop Local PostgreSQL

Stop your local PostgreSQL service:

`sudo service postgresql stop`

Start your local PostgreSQL service for local branch work:

`sudo service postgresql start` 


## Access PostgreSQL in Container

To access Postgres, in the Container tab of VS code, attach the Shell, then interminal:


```
psql -d postgres -U postgres
\l
-c postgres
\dt
```
List all databases and tables.

## Folder Structure

- **services :** Interact with the database.

- **utils :**  Common functions.

- **routers :** Contains all the routes.
- **models :** Contains the models, utilizing ORM for easier maintenance and scalability.

## Benefits of Using ORM

I leverage Object-Relational Mapping (ORM) for several advantages:

- **Simplified Querying:** Instead of writing raw queries, I interact with the database using objects, making the code more intuitive and readable.

- **Code Maintainability:** ORM makes the codebase easier to read and maintain, contributing to a more sustainable development process.

- **Database Flexibility:** ORM allows seamless switching between different databases, providing flexibility for future changes.

- **Automatic Table Creation:** Tables are automatically created based on the defined models, reducing the need for manual table creation.

- **Complex Query Avoidance:** ORM simplifies data retrieval, helping to avoid the complexity of writing intricate queries.

- **Data Validation:** ORM inherently provides data validation, ensuring data integrity and reliability.

- **Redundancy Reduction:** In the case of millions of users, ORM helps reduce redundancy for common entities such as position, location, and status. For example, it only loads the ID instead of the name for these entities in the Employee table, enhancing data retrieval efficiency.

## Django Configuration

Django is configured to read environment variables from the `.env` file and pass them to templates via context. This includes crucial information such as API keys, API key names, API URLs, and more.

## Search Array of Status

To enhance search functionality, I combine results for each status in the search array, providing a comprehensive and streamlined approach to status-based queries.

## Django Environment Configuration

Django reads environment variables from .env and sends them to templates via context.

## Scaling

To scale up, read the server's API from .env.

## Rate Limiting

Implemented simple rate limiting, using it as a decorator for a router. No external library is used for rate-limitting

## GitHub Repository Branches:

- **main, docker :** Used for running Docker Compose.
- **local :** Run locally without Docker Compose.
- **tests :** Run tests all routers.

Branches have different in API URL , import files, 

 

 