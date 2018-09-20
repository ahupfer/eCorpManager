from flask import request, redirect, render_template, flash, url_for
from flask_login import current_user, login_user, login_required, logout_user
from forms import LoginForm, RegisterForm

from app import db
from .. models import User
from . import auth

# login route for webapp users

@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Infalid email or Password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=0)
        return redirect(url_for('main.index'))

    return render_template('auth/login.html', form=form, current_user = current_user)

# register route for webapp users

@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Concratulations, you are now a registered user!')
        return(url_for('auth.login'))
    return render_template('auth/register.html', title="Register", form=form)\

# logout webapp users

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))