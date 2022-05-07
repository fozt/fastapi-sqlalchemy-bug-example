## Problem
On sqlalchemy==1.4.36 the relationships to other tables does not work, even the parameter `sa_relationship_kwargs={"lazy": "selectin"}` does not solve the problem
On version 1.4.35 code works

## Launch
1. Copy poetry.lock.invalid/pyproject.toml.invalid or poetry.lock.valid/pyproject.toml.valid files to poetry.lock/pyproject.toml
2. Run server
```sh
cp .env.example .env && docker-compose up --build
```
3. Get valid answer (sqlalchemy==1.4.35)
```sh
curl -X 'GET' 'http://localhost:8000/get-user' -H 'accept: application/json'
```
4. Internal Server Error (sqlalchemy==1.4.36)
```sh
curl -X 'GET' 'http://localhost:8001/get-user' -H 'accept: application/json'
``` 