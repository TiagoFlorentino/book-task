import sqlite3
from sqlite3 import Connection


def get_db_connection(database_name: str) -> Connection:
    db_connection = sqlite3.connect(database_name)
    db_connection.row_factory = sqlite3.Row
    return db_connection
