-- Authored fixture (CS50x Anzali, D59/D72): a tiny registrants table shaped like the lecture's froshims.db. Not official data.
CREATE TABLE registrants (id INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id));
INSERT INTO registrants (name, sport) VALUES ('Alice', 'Soccer');
INSERT INTO registrants (name, sport) VALUES ('Bob', 'Volleyball');
