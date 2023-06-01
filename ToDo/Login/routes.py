from flask import blueprints, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from ToDo.forms import LoginForm, RegisterForm
from ToDo.models import select_users_by_username, select_users_by_email, register_user

Login = blueprints.Blueprint('Login', __name__)

@Login.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in!", category='error')
        return redirect(url_for('Views.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = select_users_by_username(form.username.data)
        if user != None and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            flash("Login successful!", category='success')
            return redirect(url_for('Views.home'))
        else:
            flash("Login unsuccessful! Please check username and password", category='error')
    return render_template('login.html', form=form, user=current_user)

@Login.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("You are already logged in!", category='error')
        return redirect(url_for('Views.home'))

    form = RegisterForm()

    if form.validate_on_submit():
        if select_users_by_username(form.username.data):
            flash("Username already exists!", category='error')
        elif select_users_by_email(form.email.data):
            flash("Email already exists!", category='error')
        else:
            register_user(form.username.data, form.email.data, form.password.data)
            flash("Account created successfully!", category='success')
            return redirect(url_for('Login.login'))

    elif form.username.errors:
        flash ("Username Errors:" + str(form.username.errors), category='error')
    elif form.email.errors:
        flash("Email Errors:" + str(form.email.errors), category='error')
    elif form.password.errors:
        flash("Password Errors:" + str(form.password.errors), category='error')
    elif form.confirm_password.errors:
        flash("Confirm Password Errors:" + str(form.confirm_password.errors), category='error')

    return render_template('register.html', form=form, user=current_user)

@Login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('Login.login'))