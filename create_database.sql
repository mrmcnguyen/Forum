-- create_database.sql
.open bookings.db

CREATE TABLE appointments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL
);
