
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.database import get_connection

app = FastAPI(title="To-Do Application")


class TodoCreate(BaseModel):
    title: str


def create_table():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        """)


create_table()


@app.get("/")
def home():
    return {"message": "To-Do API is running!"}


@app.get("/todos")
def get_todos():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM todos ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]


@app.post("/todos")
def add_todo(todo: TodoCreate):
    title = todo.title.strip()

    if not title:
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO todos (title) VALUES (?)",
            (title,)
        )
        todo_id = cursor.lastrowid
        row = conn.execute(
            "SELECT * FROM todos WHERE id = ?", (todo_id,)
        ).fetchone()
        return dict(row)


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int):
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE todos SET completed = NOT completed WHERE id = ?",
            (todo_id,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")

        row = conn.execute(
            "SELECT * FROM todos WHERE id = ?", (todo_id,)
        ).fetchone()
        return dict(row)


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM todos WHERE id = ?", (todo_id,)
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
