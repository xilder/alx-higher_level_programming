-- creates a database and a table in it

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256)
);
