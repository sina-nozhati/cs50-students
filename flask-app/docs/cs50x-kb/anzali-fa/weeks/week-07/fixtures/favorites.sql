-- CS50x Anzali, Week 7 authored fixture: favorites
-- origin: authored (invented values for practice; not official CS50 or IMDb data)
-- build: sqlite3 favorites.db < favorites.sql
CREATE TABLE favorites (
    "Timestamp" TEXT,
    language TEXT,
    problem TEXT
);
INSERT INTO favorites ("Timestamp", language, problem) VALUES
    ('10/20/2025 13:01:01', 'Python', 'Hello, World'),
    ('10/20/2025 13:01:05', 'C', 'Hello, World'),
    ('10/20/2025 13:01:09', 'Scratch', 'Scratch'),
    ('10/20/2025 13:01:12', 'Python', 'DNA'),
    ('10/20/2025 13:01:20', 'C', 'Mario'),
    ('10/20/2025 13:01:31', 'Python', 'Hello, World'),
    ('10/20/2025 13:01:40', 'C', 'Hello, It''s Me'),
    ('10/20/2025 13:01:44', 'Python', 'Readability'),
    ('10/20/2025 13:01:52', 'C', 'Filter'),
    ('10/20/2025 13:02:03', 'Python', 'Mario'),
    ('10/20/2025 13:02:15', 'Scratch', 'Scratch'),
    (NULL, 'Python', 'Speller');
