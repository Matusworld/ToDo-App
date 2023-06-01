from flask import blueprints, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from ToDo.models import User, select_todo_lists, insert_todo_list
from ToDo.forms import TodoListForm

Views = blueprints.Blueprint('Views', __name__)

@Views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    user = User(current_user)
    todo_list = select_todo_lists(user)
    print(todo_list)

    form = TodoListForm()

    if form.validate_on_submit():
        insert_todo_list(form.title.data, user)
        flash("Todo List created successfully!", category='success')
        return redirect(url_for('Views.home'))

    return render_template('home.html', form=form, user=current_user, todo_list=todo_list)