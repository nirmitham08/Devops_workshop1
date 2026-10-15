
# To-Do Application

A simple To-Do application built using HTML, CSS, JavaScript, and FastAPI.

## Features

- Add tasks
- View the task list
- Delete tasks
- Display the task count
- REST API using FastAPI
- Docker support for the frontend

## Technologies Used

- HTML
- CSS
- JavaScript
- Python
- FastAPI
- Uvicorn
- Docker
- Git and GitHub

## Project Structure

```text
ToDo/
├── app/
│   ├── main.py
│   └── database.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── Dockerfile
├── .dockerignore
├── .gitignore
└── requirements.txt
```

## Run the Backend

Activate the virtual environment and install the dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open the API documentation at:

http://127.0.0.1:8000/docs

## Run the Frontend with Docker

Build the Docker image:

```bash
docker build -t todo-app .
```

Run the container:

```bash
docker run -d -p 8080:80 --name todo-container todo-app
```

Open the application at:

http://localhost:8080
