# SWAPI Wrapper

A simple Python REST API wrapper for the Star Wars API (SWAPI), deployed live on Heroku.  
Easily retrieve data about films, characters, and starships from the Star Wars universe.

**Live Demo:** [https://swapi-wrapper-363d14325093.herokuapp.com/](https://swapi-wrapper-363d14325093.herokuapp.com/)

---

## Features

- Retrieve a list of Star Wars films.
- Retrieve a list of characters (people) for a specific film.
- Retrieve a list of starships for a specific film.
- Caching to optimize response times when requesting the same resource within a 5-minute window.
- Rate limiting to control API usage.
- Dockerfile for running the application inside a Docker container.
- Endpoint authentication with JWT.
- Accessible through a live URL on Heroku.

---

## Prerequisites

- Python 3.8+
- pip
- Install all dependencies via `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
---

## Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/domkoekie/SWAPI_wrapper.git
cd SWAPI_wrapper
```

2. **Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Run Locally**

```bash
python app.py
```

---

## Architecture & Design

- **Framework**: 
  - Built using **Flask**, a lightweight Python web framework for creating RESTful endpoints.
  
- **Authentication**: 
  - JWT authentication implemented via `flask-jwt-extended`.
  - Secures endpoints by requiring clients to log in and include a valid token in requests.

- **Rate Limiting**: 
  - `flask-limiter` prevents abuse by limiting the number of requests a user can make within a given time frame.

- **Caching**: 
  - Responses from the SWAPI are cached locally using **Flask-Caching** with a 5-minute TTL.

- **Endpoints**: 
  - `GET /films` → List all films  
  - `GET /films/{id}/characters` → List characters for a specific film  
  - `GET /films/{id}/starships` → List starships for a specific film  
  - `POST /login` → Authenticate user and receive JWT

- **Error Handling**: 
  - Returns meaningful HTTP status codes and messages for invalid requests.

- **Containerization**: 
  - Dockerfile included for running the application in a containerized environment.

- **Deployment**: 
  - Hosted on **Heroku**, with **Gunicorn** as the WSGI server in production.

- **Design Decisions**: 
  - Flask chosen for simplicity and lightweight nature.  
  - JWT authentication secures endpoints.  
  - Caching and rate limiting optimize performance and meet bonus requirements.
  - Docker and Heroku deployment ensure portability and ease of testing.
 
---
  
## Docker

Build and run the Docker container

```bash
docker build -t swapi-wrapper .
docker run -p 5000:5000 swapi-wrapper
```

**Visit:** http://localhost:5000/

---

## Endpoints

- **GET /films** - Returns a list of Star Wars films.  
- **GET /films/{id}/characters** - Returns a list of characters for the specified film.  
- **GET /films/{id}/starships** - Returns a list of starships for the specified film.  
- **POST /login** - Authenticate a user and receive a JWT token.  

---

## Authentication

Use the following credentials for JWT login:

- **Username:** graduate  
- **Password:** ilovesenwes  

**Example Requests:**

**Get a JWT token by logging in**

```powershell
$body = @{
    username = "graduate"
    password = "ilovesenwes"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri http://localhost:5000/login -Method POST -Body $body -ContentType "application/json"

$token = $response.access_token
```

**Use the JWT token to access other endpoints**

```powershell
Invoke-RestMethod -Uri http://localhost:5000/films -Method GET -Headers @{Authorization = "Bearer $token"}
```

---

## Deployment (Heroku)

```bash
heroku create swapi-wrapper
git push heroku master
heroku ps:scale web=1
heroku logs --tail --app swapi-wrapper
```

---

## License

This project is licensed under the MIT License.
