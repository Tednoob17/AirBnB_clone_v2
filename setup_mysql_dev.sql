-- Type: SQL
-- Author: Hamidou TESSILIMI, Student at ALX
-- Created: 2016-09-28 10:00:00
-- Updated: 2016-09-28 10:00:00
-- Description: Setup MySQL dev database

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
