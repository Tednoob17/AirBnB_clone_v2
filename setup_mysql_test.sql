-- Type: SQL
-- Author: Hamidou TESSILIMI, Student at ALX
-- Created: 2016-09-28 10:00:00
-- Updated: 2016-09-28 10:00:00
-- Description: Setup MySQL test database

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
