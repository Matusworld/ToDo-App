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

-- Sample data
-- Users
INSERT INTO Users (username, email, password) VALUES ('Mat', 'mat@gmail.com', '123');
INSERT INTO Users (username, email, password) VALUES ('DIS', 'dis@gmail.com', 'DIS');
INSERT INTO Users (username, email, password) VALUES ('UIS', 'uis@gmail.com', 'UIS');

-- ToDo List
INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Stay Hydrated', 'NOW()', 1);
INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Vitamins', 'NOW()', 1);
INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Meal Plan', 'NOW()', 1);
INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Study for DIS', 'NOW()', 1);

INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Stay Hydrated', 'NOW()', 2);
INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Create Exam (Only Easy Questions)', 'NOW()', 2);
INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Last Lecture Of The Course', 'NOW()', 2);
INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Q&A session', 'NOW()', 2);

INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Stay Hydrated', 'NOW()', 3);
INSERT INTO todo_list (title, creation_date, user_id) VALUES ('Lecture About MUST 4 Phases', 'NOW()', 3);

-- Tasks
INSERT INTO tasks (description, todo_list_id) VALUES ('Drink 3.7L Of Water', 1);

INSERT INTO tasks (description, todo_list_id) VALUES ('Multivitamin', 2);
INSERT INTO tasks (description, todo_list_id) VALUES ('Vitamin D', 2);
INSERT INTO tasks (description, todo_list_id) VALUES ('Omega 3 Fish Oil', 2);

INSERT INTO tasks (description, todo_list_id) VALUES ('Eat Breakfast, At 8', 3);
INSERT INTO tasks (description, todo_list_id) VALUES ('Eat Apple, At 10', 3);
INSERT INTO tasks (description, todo_list_id) VALUES ('Eat Lunch, At 12', 3);
INSERT INTO tasks (description, todo_list_id) VALUES ('Eat Fruit Biscuts, At 14', 3);
INSERT INTO tasks (description, todo_list_id) VALUES ('Eat Dinner, At 18', 3);
INSERT INTO tasks (description, todo_list_id) VALUES ('Protein Shake and a Snack, At 22', 3);

INSERT INTO tasks (description, todo_list_id) VALUES ('E/R Modeling', 4);
INSERT INTO tasks (description, todo_list_id) VALUES ('Relational Calculus', 4);
INSERT INTO tasks (description, todo_list_id) VALUES ('Relational Algebra', 4);
INSERT INTO tasks (description, todo_list_id) VALUES ('SQL', 4);
INSERT INTO tasks (description, todo_list_id) VALUES ('Normal Forms', 4);
INSERT INTO tasks (description, todo_list_id) VALUES ('Functional Dependencies', 4);
INSERT INTO tasks (description, todo_list_id) VALUES ('Views', 4);
INSERT INTO tasks (description, todo_list_id) VALUES ('Triggers', 4);
INSERT INTO tasks (description, todo_list_id) VALUES ('Indices', 4);

INSERT INTO tasks (description, todo_list_id) VALUES ('Drink 3.7L Of Water', 5);
INSERT INTO tasks (description, todo_list_id) VALUES ('Question 1', 6);
INSERT INTO tasks (description, todo_list_id) VALUES ('Question 2', 6);

INSERT INTO tasks (description, todo_list_id) VALUES ('Recap', 7);

INSERT INTO Tasks (description, todo_list_id) VALUES ('Create Absalon Announcement', 8);

INSERT INTO tasks (description, todo_list_id) VALUES ('Drink 3.7L Of Water', 9);
INSERT INTO tasks (description, todo_list_id) VALUES ('Create Slides', 10);
INSERT INTO tasks (description, todo_list_id) VALUES ('Initiation Phase', 10);
INSERT INTO tasks (description, todo_list_id) VALUES ('In-Line Analysis', 10);
INSERT INTO tasks (description, todo_list_id) VALUES ('In-Depth Analysis', 10);
INSERT INTO tasks (description, todo_list_id) VALUES ('Innovation Phase', 10);