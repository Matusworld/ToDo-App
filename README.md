# ToDo-App

## Usage

In our simple todo app, you start by creating a user and afterwards you can create todo lists, which can be deleted or viewed.<br>
You can add tasks for todo lists and mark them off as completed or delete them. The front page will show all your todo lists and
how many tasks are for each list and how many are completed. <br> Deleting a todo list will cascade delete all related tasks and deleting a user will 
delete all related todo lists and tasks.

<b>Sample users:</b><br>
username: Mat<br>
password: 123<br>
<br>
username: DIS<br>
password: DIS<br>
<br>
username: UIS<br>
password: UIS

## Setup

### Requirements

From root:&nbsp;&nbsp;`pip install -r requirements.txt`

### Database

Set the database in the __init__.py file

Run schema.sql in your database to create the tables and sample data

### Running

Run with:&nbsp;&nbsp;`python run.py` (It should be python 3)