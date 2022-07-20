DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS campaigns;
DROP TABLE IF EXISTS campaign_log;

CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    active TEXT NOT NULL
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
    campaign_id REFERENCES campaigns(id),
    client_id REFERENCES clients(id)
);