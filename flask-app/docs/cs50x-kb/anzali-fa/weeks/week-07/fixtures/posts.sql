-- CS50x Anzali, Week 7 authored fixture: posts
-- origin: authored (invented values for practice; not official CS50 or IMDb data)
-- build: sqlite3 posts.db < posts.sql
CREATE TABLE posts (
    id INTEGER,
    likes INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY(id)
);
INSERT INTO posts (id, likes) VALUES
    (1, 10),
    (2, 0);
