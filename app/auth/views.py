from flask import request, redirect, render_template, flash, url_for
from flask_login import current_user, login_user, login_required
from forms import LoginForm

from .. models import User
from . import auth


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

    return render_template('login.html', form=form, current_user = current_user)

