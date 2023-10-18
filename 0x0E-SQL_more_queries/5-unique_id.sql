-- creates a new table in a named datarbase

CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
