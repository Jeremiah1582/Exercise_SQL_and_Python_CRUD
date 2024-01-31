-- Task 3: Create Tables
CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY,
    author_name TEXT NOT NULL
);

CREATE TABLE publishers (
    publisher_id INTEGER PRIMARY KEY,
    publisher_name TEXT NOT NULL
);

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    publication_year INTEGER,
    author_id INTEGER,
    publisher_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors (author_id),
    FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
);

-- Task 4: Insert Data
INSERT INTO authors (author_name) VALUES ('John Doe'), ('Jane Smith'), ('Mark Johnson');

INSERT INTO publishers (publisher_name) VALUES ('Book House'), ('Readers Publishing'), ('Tech Books');

INSERT INTO books (title, publication_year, author_id, publisher_id) VALUES
('Python Fundamentals', 2021, 1, 1),
('Data Science for Beginners', 2020, 2, 2),
('Introduction to SQL', 2018, 3, 3);

-- Task 5: Retrieve Data
SELECT * FROM authors;
SELECT * FROM publishers;
SELECT * FROM books;

-- Task 6: Update and Delete
UPDATE authors SET author_name = 'New Author' WHERE author_id = 1;
DELETE FROM publishers WHERE publisher_id = 2;