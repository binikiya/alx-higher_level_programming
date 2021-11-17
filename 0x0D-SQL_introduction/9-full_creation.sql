-- Creates a new table called second_table
-- It doesn't print error if it fails
-- Insert new four values(rows) into second_tables

CREATE TABLE IF NOT EXISTS second_table (id INT,
name VARCHAR(256),
score INT);

INSERT INTO second_table (id , name, score)
VALUES (1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
