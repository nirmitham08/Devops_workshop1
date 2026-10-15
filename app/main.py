
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="To-Do Application API")

# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = []
next_id = 1


class TodoCreate(BaseModel):
    title: str


@app.get("/")
def home():
    return {"message": "To-Do Application API is running"}


@app.get("/todos")
def get_todos():
    return tasks


@app.post("/todos", status_code=201)
def add_todo(todo: TodoCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": todo.title,
    }

    tasks.append(new_task)
    next_id += 1

    return new_task


@app.delete("/todos/{task_id}")
def delete_todo(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
