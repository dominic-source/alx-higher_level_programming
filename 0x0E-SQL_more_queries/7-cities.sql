-- create database and cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT NOT EXIST hbtn_0d_usa.cities(
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id INT NOT NULL FOREIGN KEY(id) REFERENCE states(id),
       name VARCHAR(256) NOT NULL);
