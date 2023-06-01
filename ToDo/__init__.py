import psycopg2
from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gfjfgtretrehfggh245354342d'

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="TodoApp",
    user="postgres",
    password="DIS"
)

# Login Manager
LoginManager = LoginManager(app)
LoginManager.login_view = 'Login.login'
LoginManager.login_message_category = 'info'

from ToDo.Views.routes import Views
from ToDo.Login.routes import Login

app.register_blueprint(Views)
app.register_blueprint(Login)

# Task is still not implemented
# View button needs to be implemented
# Delete button needs to be implemented

# A interesting SQL query could be to get all the tasks that a user has to do, diffent route for this called all tasks

# design is ugly xD

# small things:
# would be nice if usernames was not case sensitive
# add a trigger that logs every sql query that is executed and who executed it, and what time it was executed, and what the result was