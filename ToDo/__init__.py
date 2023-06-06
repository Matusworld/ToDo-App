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