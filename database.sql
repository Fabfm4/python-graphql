CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    height FLOAT,
    is_student BOOLEAN
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
);

INSERT INTO persons (name, age, height, is_student) VALUES
('Alice', 23, 5.5, 1),
('Bob', 30, 6.0, 0),
('Charlie', 19, 5.8, 1);

INSERT INTO books (title, author) VALUES
('1984', 'George Orwell'),
('To Kill a Mockingbird', 'Harper Lee'),
('The Great Gatsby', 'F. Scott Fitzgerald');