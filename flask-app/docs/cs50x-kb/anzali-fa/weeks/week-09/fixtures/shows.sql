-- Authored fixture (CS50x Anzali, D59/D72): a tiny shows table shaped like the lecture's shows.db. Not official data.
CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, year NUMERIC, episodes INTEGER, PRIMARY KEY(id));
INSERT INTO shows (title, year, episodes) VALUES ('The Office', 2005, 188);
INSERT INTO shows (title, year, episodes) VALUES ('Office Ladies', 2019, NULL);
INSERT INTO shows (title, year, episodes) VALUES ('Friends', 1994, 236);
