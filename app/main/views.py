from . import main
from .. models import EveChar
from flask import render_template
from flask_login import current_user

@main.route('/')
def index():
    if current_user.is_authenticated:
        chars = EveChar.query.filter_by(user_id=current_user.id).all()
        return render_template('index.html', chars=chars)
    return render_template('index.html')