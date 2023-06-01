from ToDo import conn, LoginManager
from flask_login import UserMixin

@LoginManager.user_loader
def load_user(user_id):
    cur = conn.cursor()

    user_sql = """
        SELECT * FROM users WHERE id = %s
    """

    cur.execute(user_sql, (user_id,))
    user = User(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return user

def register_user(username, email, password):
    cur = conn.cursor()

    user_sql = """
        INSERT INTO users (username, email, password) VALUES (%s, %s, %s)
    """

    cur.execute(user_sql, (username, email, password))
    conn.commit()
    cur.close()

# The same as load_user but with username
def select_users_by_username(username):
    cur = conn.cursor()

    user_sql = """
        SELECT * FROM users WHERE username = %s
    """

    cur.execute(user_sql, (username,))
    user = User(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return user

def select_users_by_email(email):
    cur = conn.cursor()

    user_sql = """
        SELECT * FROM users WHERE email = %s
    """

    cur.execute(user_sql, (email,))
    user = cur.fetchone() if cur.rowcount > 0 else None
    cur.close()
    return user

def insert_todo_list(title, user):
    cur = conn.cursor()

    todo_list_sql = """
        INSERT INTO todo_list (title, creation_date, user_id) VALUES (%s, NOW(), %s)
    """

    cur.execute(todo_list_sql, (title, user.userId))
    conn.commit()
    cur.close()

def insert_task(description, todo_list):
    cur = conn.cursor()

    task_sql = """
        INSERT INTO tasks (description, todo_list_id) VALUES (%s, %s)
    """

    cur.execute(task_sql, (description, False, todo_list))
    conn.commit()
    cur.close()

def select_todo_lists(user):
    cur = conn.cursor()

    todo_list_sql = """
        SELECT * FROM todo_list WHERE user_id = %s
    """

    cur.execute(todo_list_sql, (user.userId,))
    todo_lists = cur.fetchall()
    cur.close()
    return todo_lists

class User(tuple, UserMixin):
    def __init__(self, user_data):
        self.userId = user_data[0]
        self.username = user_data[1]
        self.email = user_data[2]
        self.password = user_data[3]
        super().__init__()
    
    def get_id(self):
        return self.userId
    
class TodoList(tuple):
    def __init__(self, todo_list_data):
        self.todo_list_id = todo_list_data[0]
        self.title = todo_list_data[1]
        self.creation_date = todo_list_data[2]
        self.user_id = todo_list_data[3]

class Task(tuple):
    def __init__(self, task_data):
        self.task_id = task_data[0]
        self.description = task_data[1]
        self.completed = task_data[2]
        self.todo_list_id = task_data[3]