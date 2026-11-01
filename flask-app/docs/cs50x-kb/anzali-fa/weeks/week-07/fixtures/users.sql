-- CS50x Anzali, Week 7 authored fixture: users
-- origin: authored (invented values for practice; not official CS50 or IMDb data)
-- build: sqlite3 users.db < users.sql
CREATE TABLE users (
    id INTEGER,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    PRIMARY KEY(id)
);
-- Plain-text passwords only to keep the injection demo small; real apps store hashes (Week 9).
INSERT INTO users (id, username, password) VALUES
    (1, 'malan', 'apple'),
    (2, 'kelly', 'banana'),
    (3, 'sina', 'cherry');
