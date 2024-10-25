CREATE TABLE IF NOT EXISTS users
(
    id TEXT PRIMARY KEY,
    fullname TEXT,
    email TEXT,
    location TEXT,
    age int
);
BEGIN;

INSERT INTO users (id, fullname, email, location, age)
VALUES 
    ('31fcc7c6-2558-4487-adee-aae427f06aa9', 'Alice Johnson', 'alice.johnson@example.com', 'New York', 28),
    ('46877016-3e24-454d-9e04-89a720b08625', 'Bob Smith', 'bob.smith@example.com', 'San Francisco', 34),
    ('586c07d1-d55c-4cd8-9839-a02c7cb29a5e', 'Charlie Brown', 'charlie.brown@example.com', 'Chicago', 22),
    ('14c764c3-20fc-4408-a4ae-6bb2276d2486', 'Diana Prince', 'diana.prince@example.com', 'Washington D.C.', 30),
    ('9b940b37-a230-41e8-8d00-81217847feb8', 'Ethan Hunt', 'ethan.hunt@example.com', 'Los Angeles', 40);
COMMIT;