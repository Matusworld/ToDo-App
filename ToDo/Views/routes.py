from flask import blueprints, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from ToDo.models import User, Task, select_todo_lists, insert_todo_list, select_tasks, get_todo_list, insert_task, delete_todo_list, delete_task, get_task, update_task, todo_lists_task_count, select_all_tasks_by_userId
from ToDo.forms import TodoListForm, TaskForm

Views = blueprints.Blueprint('Views', __name__)

@Views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    user = User(current_user)

    todo_lists = todo_lists_task_count(user)

    form = TodoListForm()

    if form.validate_on_submit():
        insert_todo_list(form.title.data, user)
        flash("Todo List created successfully!", category='success')
        return redirect(url_for('Views.home'))

    return render_template('home.html', form=form, user=current_user, todo_list=todo_lists)

@Views.route('/<int:todo_list_id>', methods=['GET', 'POST'])
@login_required
def todo_list_delete(todo_list_id):
    
    delete_todo_list(todo_list_id)

    return redirect(url_for('Views.home'))


@Views.route('/todo_list/delete/<int:task_id>', methods=['GET', 'POST'])
@login_required
def task_delete(task_id):

    todo_list_id = get_task(task_id).todo_list_id
    
    delete_task(task_id)

    return redirect(request.referrer)

@Views.route('/todo_list/update/<int:task_id>', methods=['GET', 'POST'])
@login_required
def task_update(task_id):

    task  = get_task(task_id)

    update_task(task)
    
    return redirect(request.referrer)

@Views.route('/todo_list/<int:todo_list_id>', methods=['GET', 'POST'])
@login_required
def tasks(todo_list_id):
    user = User(current_user)    

    tasks = select_tasks(todo_list_id)
    todo_list = get_todo_list(todo_list_id)

    form = TaskForm()

    if form.validate_on_submit():
        insert_task(form.description.data, todo_list_id)
        flash("Task created successfully!", category='success')
        return redirect(url_for('Views.tasks', todo_list_id=todo_list_id))

    return render_template('tasks.html', user=current_user, form=form, todo_list=todo_list, tasks=tasks)

@Views.route('/todo_list/all_tasks', methods=['GET', 'POST'])
@login_required
def all_tasks():
    user = User(current_user)

    all_tasks = select_all_tasks_by_userId(user.userId)

    return render_template('all_tasks.html', user=current_user, tasks=all_tasks)
