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
        "INSERT INTO clients (name, active) VALUES (?, ?)", ("JOAO MANUEL", 1)
    )
    db_cursor.execute(
        "INSERT INTO clients (name, active) VALUES (?, ?)", ("JOAO JOSE", 0)
    )
    # Add a new book
    db_cursor.execute(
        "INSERT INTO books (title, status) VALUES (?, ?)", ("A Aventura 1", "AVAILABLE")
    )
    db_cursor.execute(
        "INSERT INTO books (title, status) VALUES (?, ?)", ("A Aventura 2", "AVAILABLE")
    )
    db_cursor.execute(
        "INSERT INTO books (title, status) VALUES (?, ?)",
        ("A Aventura 3", "DISCONTINUED"),
    )
    db_cursor.execute(
        "INSERT INTO partners (name, email, active) VALUES (?, ?, ?)",
        ("Mahna Mahna", "mahna_mahna@abc.com", 1),
    )
    db_cursor.execute(
        "INSERT INTO partner_log (partner_id, active) VALUES (?, ?)",
        (1, 1),
    )
    db_cursor.execute(
        "INSERT INTO campaigns (name, slogan, partner_id) VALUES (?, ?, ?)",
        ("SUMMER READING", "READ WITH US", 1),
    )
    db_cursor.execute(
        "INSERT INTO campaign_log (campaign_id, client_id, new_client) VALUES (?, ?, ?)",
        (1, 1, 1),
    )
    connection.commit()
    connection.close()
    print("Closing DB Connection - Shutdown!")


def database_startup_for_testing():
    print("Generating testing base DB!")
    connection = sqlite3.connect("test_db.db")
    with open("book_task/database/schema.sql") as f:
        # Read Schema
        connection.executescript(f.read())
    connection.commit()
    connection.close()
    print("Closing DB Connection - Shutdown!")


database_startup()
database_startup_for_testing()
