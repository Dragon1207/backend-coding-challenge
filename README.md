# Challenge

This challenge is divided between the main task and additional stretch goals. All of those stretch goals are optional, but we would love to see them implemented. It is expected that you should be able to finish the challenge in about 1.5 hours. If you feel you are not able to implement everything on time, please, try instead describing how you would solve the points you didn't finish.

And also, please do not hesitate to ask any questions. Good luck!

## gistapi

Gistapi is a simple HTTP API server implemented in Flask for searching a user's public Github Gists.
The existing code already implements most of the Flask boilerplate for you.
The main functionality is left for you to implement.
The goal is to implement an endpoint that searches a user's Gists with a regular expression.
For example, I'd like to know all Gists for user `justdionysus` that contain the pattern `import requests`.
The code in `gistapi.py` contains some comments to help you find your way.

To complete the challenge, you'll have to write some HTTP queries from `Gistapi` to the Github API to pull down each Gist for the target user.
Please don't use a github API client (i.e. using a basic HTTP library like requests or aiohttp or urllib3 is fine but not PyGithub or similar).


## Stretch goals

* Implement a few tests (using a testing framework of your choice)
* In all places where it makes sense, implement data validation, error handling, pagination
* Migrate from `requirements.txt` to `pyproject.toml` (e.g. using [poetry](https://python-poetry.org/))
* Implement a simple Dockerfile
* Implement handling of huge gists
* Set up the necessary tools to ensure code quality (feel free to pick up a set of tools you personally prefer)
* Document how to start the application, how to build the docker image, how to run tests, and (optionally) how to run code quality checkers
* Prepare a TODO.md file describing possible further improvements to the archtiecture:
    - Can we use a database? What for? SQL or NoSQL?
    - How can we protect the api from abusing it?
    - How can we deploy the application in a cloud environment?
    - How can we be sure the application is alive and works as expected when deployed into a cloud environment?
    - Any other topics you may find interesting and/or important to cover


# DEVELOPMENT INSTRUCTIONS

## Environment Setup Locally

### Pre-requisites

* git
* Python (3.9.6)
* [Poetry](https://python-poetry.org/docs/)

### Steps

1. Use a python virtual environment (optional but recommended).
    ```bash
    python -m venv venv  # Create new virtual environment
    source venv/bin/activate  # Activate the environment
    ```
2. Install python dependencies in the root folder.

    Method 1:
    ```bash
    poetry lock # this command is optional. you can run this after you add new dependencies on pyproject.toml file
    poetry install
    ```
    Method 2:
    If you want to install python dependencies using pip, you can run
    ```bash
    pip install -r requirements.txt
    ```
3. Start your local server.

    Method 1 (using Poetry):
    ```bash
    poetry run python gistapi/gistapi.py
    ```
    Method 2 (using flask cli):
    ```bash
    flask --app gistapi run --port=9876
    ```
    Method 3 (using python )
    ```bash
    python gistapi/gistapi.py
    ```
4. Run tests

    ```bash
    pytest
    ```
5. Run code quality checkers
    ```bash
    flake8 .
    black .
    ```
## Environment Setup using Docker

### Pre-requisites

* git
* Docker (Please make sure Docker is installed on your pc correctly using `docker ps` command)

### Steps

1. Build docker image.
    ```bash
    # Run this command in the root folder
    docker build -t gistapi .
    ```
2. Create docker container with specific name
    ```bash
    docker create --name gistapi-container -p 9876:9876 gistapi
    ```
3. Start (Run) Docker container
    ```bash
    docker start gistapi-container
    ```
    Now the docker container is running.
    
    If you want to check the log,
    ```bash
    docker logs --follow gistapi-container
    ```
4. Run tests
    ```bash
    docker exec -it gistapi-container pytest
    ```
5. Run code quality checkers
    ```bash
    docker exec -it gistapi-container black .
    docker exec -it gistapi-container flake8 .
    ```
6. Stop Docker container
    ```bash
    docker stop gistapi-container
    ```
7. Remove Docker container
     ```bash
    docker rm gistapi-container
    ```