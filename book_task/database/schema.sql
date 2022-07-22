DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS campaigns;
DROP TABLE IF EXISTS campaign_log;
DROP TABLE IF EXISTS renting_log;
DROP TABLE IF EXISTS partners;
DROP TABLE IF EXISTS partner_log;

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

CREATE TABLE renting_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id REFERENCES books(id),
    client_id REFERENCES clients(id),
    rented_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    slogan TEXT NOT NULL,
    partner_id REFERENCES partners(id)
);

CREATE TABLE campaign_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    new_client INTEGER,
    campaign_id REFERENCES campaigns(id),
    client_id REFERENCES clients(id)
);

CREATE TABLE partners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    active INTEGER,
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE partner_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    partner_id REFERENCES partners(id),
    update_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    active INTEGER
);
