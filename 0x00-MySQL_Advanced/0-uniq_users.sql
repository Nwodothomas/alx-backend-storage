-- A SQL script that creates a table (called users) with following fields
-- id, email, name
CREATE TABLE IF NOT EXISTS users (
README.md id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
README.md email varchar(255) NOT NULL UNIQUE,
README.md name varchar(255)
)
