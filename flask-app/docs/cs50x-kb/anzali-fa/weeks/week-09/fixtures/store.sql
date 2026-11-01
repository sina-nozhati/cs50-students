-- Authored fixture (CS50x Anzali, D59/D72): a tiny books table shaped like the lecture's store.db. Not official data.
CREATE TABLE books (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id));
INSERT INTO books (title) VALUES ('Book A');
INSERT INTO books (title) VALUES ('Book B');
INSERT INTO books (title) VALUES ('Book C');
