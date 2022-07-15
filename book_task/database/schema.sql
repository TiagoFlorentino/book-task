DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS clients;

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    status TEXT NOT NULL,
    renter_id INTEGER
);

CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    active TEXT NOT NULL
);

