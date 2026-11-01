-- CS50x Anzali, Week 7 authored fixture: library
-- origin: authored (invented values for practice; not official CS50 or IMDb data)
-- build: sqlite3 library.db < library.sql
CREATE TABLE authors (
    id INTEGER,
    name TEXT NOT NULL,
    PRIMARY KEY(id)
);
CREATE TABLE books (
    id INTEGER,
    title TEXT NOT NULL,
    year INTEGER,
    pages INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE authorship (
    book_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(author_id) REFERENCES authors(id)
);
CREATE TABLE loans (
    id INTEGER,
    book_id INTEGER NOT NULL,
    member TEXT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(book_id) REFERENCES books(id)
);
INSERT INTO authors (id, name) VALUES
    (1, 'Ada'),
    (2, 'Babak'),
    (3, 'Chen'),
    (4, 'Dara');
INSERT INTO books (id, title, year, pages) VALUES
    (1, 'Arrays and Beyond', 2019, 240),
    (2, 'Binary Trees', 2021, 310),
    (3, 'C in Practice', 2018, 420),
    (4, 'Data at Scale', 2023, 280),
    (5, 'Everyday SQL', 2022, 190);
INSERT INTO authorship (book_id, author_id) VALUES
    (1, 1),
    (2, 1),
    (2, 2),
    (3, 3),
    (4, 2),
    (4, 4),
    (5, 4);
INSERT INTO loans (id, book_id, member) VALUES
    (1, 1, 'Sara'),
    (2, 3, 'Reza'),
    (3, 3, 'Sara'),
    (4, 5, 'Nima'),
    (5, 3, 'Nima'),
    (6, 2, 'Sara');
