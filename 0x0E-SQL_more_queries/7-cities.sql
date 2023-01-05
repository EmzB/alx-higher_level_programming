-- Query to create db and entries
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa; -- creating the database
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities ( -- creating cities
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states(id));
