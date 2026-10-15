
import os
import sqlite3
from pathlib import Path

DATABASE_PATH = os.getenv("TODO_DB_PATH", "todos.db")


def get_connection():
    """Create a connection to the SQLite database."""
    db_path = Path(DATABASE_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(str(db_path))
    connection.row_factory = sqlite3.Row
    return connection
