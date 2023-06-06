DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS todo_list;
DROP TABLE IF EXISTS Users;

CREATE TABLE IF NOT EXISTS Users(
	id SERIAL PRIMARY KEY,
	username VARCHAR(255) UNIQUE NOT NULL,
	email VARCHAR(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS todo_list(
	id SERIAL PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	creation_date DATE NOT NULL,
	user_id INTEGER NOT NULL,
	FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tasks(
	taskId SERIAL PRIMARY KEY,
	description VARCHAR(255) NOT NULL,
	completed BOOLEAN default false,
	todo_list_id INTEGER NOT NULL,
	FOREIGN KEY (todo_list_id) REFERENCES todo_list(id) ON DELETE CASCADE
);