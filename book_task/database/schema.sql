DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS campaigns;
DROP TABLE IF EXISTS campaign_log;

CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    active INTEGER
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL,
    renter_id REFERENCES clients(id)
);

CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    slogan TEXT NOT NULL
);

CREATE TABLE campaign_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    new_client INTEGER,
    campaign_id REFERENCES campaigns(id),
    client_id REFERENCES clients(id)
);