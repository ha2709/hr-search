# hr-search Documentation

## Activate Enviroment  

To activate the virtual environment, use the following command:

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

To run docker subsequently:

`docker-compose up`

## Running Tests

To run tests:

```
source env/bin/activate
cd api
pytest
```

## Run API

To run API local, use the following command:

 `uvicorn api.main:app --reload --port 8001`


## Run Django

 

Attach Shell in Docker of Vscode tab : 

`python3 manage.py runserver`

## Run Migration

To run migrations, use :

`python3 manage.py migrate`

## Create Superuser

To create a superuser, run:

`python3 manage.py createsuperuser`

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

Start your local PostgreSQL service for testing or for running code on  local :

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

## Search API 

- Search Array of Status: To enhance search functionality, I combine results for each status in the search array, providing a comprehensive and streamlined approach to status-based queries.

- Companies search for Dynamic column ,  , I read colum data for each company or organization from `compnay_config.json`. If not company search, It will load all the columns. 


## Scaling

- For scalability, configure the server's API by reading from the .env file. If Docker is being used, the configuration should be specified in the .env.docker file. Variables from the .env file can be injected through command-line arguments, Dockerfile configurations, or via Helm charts for Kubernetes and Terraform.
- Before running Docker Compose, ensure to rename the .env.example file to .env.docker for proper configuration.

## Rate Limiting

Implemented simple rate limiting, using it as a decorator for a router. No external library is used for rate-limitting

## GitHub Repository Branches:
 
- **main, docker :** Used for running Docker Compose.
- **local :** Run locally without Docker Compose.
- **tests :** Run tests all routers.

There are many branches in my Github repository. I work alone and don't have time so I had pushed on main and other branches. It is not best practices to push to main branch.
