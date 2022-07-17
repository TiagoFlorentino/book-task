import sqlite3


def database_startup():
    print("Generating base DB!")
    connection = sqlite3.connect("database.db")
    with open("book_task/database/schema.sql") as f:
        # Read Schema
        connection.executescript(f.read())
    db_cursor = connection.cursor()
    # Add a new client
    db_cursor.execute(
        "INSERT INTO clients (name, active) VALUES (?, ?)", ("JOAO MANUEL", "TRUE")
    )
    db_cursor.execute(
        "INSERT INTO clients (name, active) VALUES (?, ?)", ("JOAO JOSE", "TRUE")
    )
    # Add a new book
    db_cursor.execute(
        "INSERT INTO books (title, status) VALUES (?, ?)", ("A Aventura 1", "IN-HOUSE")
    )
    db_cursor.execute(
        "INSERT INTO books (title, status) VALUES (?, ?)", ("A Aventura 2", "IN-HOUSE")
    )
    connection.commit()
    connection.close()
    print("Closing DB Connection - Shutdown!")


database_startup()
