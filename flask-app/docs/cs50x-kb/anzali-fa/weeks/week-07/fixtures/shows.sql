-- CS50x Anzali, Week 7 authored fixture: shows
-- origin: authored (invented values for practice; not official CS50 or IMDb data)
-- build: sqlite3 shows.db < shows.sql
CREATE TABLE shows (
    id INTEGER,
    title TEXT NOT NULL,
    year NUMERIC,
    episodes INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE ratings (
    show_id INTEGER NOT NULL,
    rating REAL NOT NULL,
    votes INTEGER NOT NULL,
    FOREIGN KEY(show_id) REFERENCES shows(id)
);
CREATE TABLE genres (
    show_id INTEGER NOT NULL,
    genre TEXT NOT NULL,
    FOREIGN KEY(show_id) REFERENCES shows(id)
);
CREATE TABLE people (
    id INTEGER,
    name TEXT NOT NULL,
    birth NUMERIC,
    PRIMARY KEY(id)
);
CREATE TABLE stars (
    show_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(show_id) REFERENCES shows(id),
    FOREIGN KEY(person_id) REFERENCES people(id)
);
INSERT INTO shows (id, title, year, episodes) VALUES
    (63881, 'Catweazle', 1970, 26),
    (290978, 'The Office', 2001, 14),
    (386676, 'The Office', 2005, 188),
    (1266020, 'Parks and Recreation', 2009, 125),
    (2467372, 'Brooklyn Nine-Nine', 2013, 153),
    (4955642, 'The Good Place', 2016, 53);
INSERT INTO ratings (show_id, rating, votes) VALUES
    (63881, 7.4, 612),
    (290978, 8.5, 150000),
    (386676, 9.0, 700000),
    (1266020, 8.6, 300000),
    (4955642, 8.2, 190000);
INSERT INTO genres (show_id, genre) VALUES
    (63881, 'Adventure'),
    (63881, 'Comedy'),
    (63881, 'Family'),
    (290978, 'Comedy'),
    (386676, 'Comedy'),
    (1266020, 'Comedy'),
    (2467372, 'Comedy'),
    (2467372, 'Crime'),
    (4955642, 'Comedy'),
    (4955642, 'Drama'),
    (4955642, 'Fantasy');
INSERT INTO people (id, name, birth) VALUES
    (1, 'Steve Carell', 1962),
    (2, 'Rainn Wilson', 1966),
    (3, 'Ricky Gervais', 1961),
    (4, 'Amy Poehler', 1971),
    (5, 'Kristen Bell', 1980),
    (6, 'Andy Samberg', 1978),
    (7, 'Geoffrey Bayldon', 1924),
    (8, 'Steve Coogan', 1965),
    (9, 'Steve Buscemi', 1957);
INSERT INTO stars (show_id, person_id) VALUES
    (386676, 1),
    (386676, 2),
    (290978, 3),
    (1266020, 4),
    (4955642, 5),
    (2467372, 6),
    (63881, 7);
