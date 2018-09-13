from datetime import datetime

from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

import time

# Webapp user definition

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))

    # Relationship
    evechars = db.relationship('EveChar', backref='evechar')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    def __repr__(self):
        return '<User %r>' % self.username

# EvE Character Model

class EveChar(db.Model):
    __tablename__ = "evechars"
    character_id = db.Column(db.BigInteger,primary_key=True,autoincrement=False)
    character_owner_hash = db.Column(db.String(100))
    character_name = db.Column(db.String(200))

    # sso Token stuf
    access_token = db.Column(db.String(100))
    access_token_expires = db.Column(db.DateTime())
    refresh_token = db.Column(db.String(100))

    # Relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def get_id(self):
        return self.character_id

    def get_sso_data(self):
        """ Little "helper" function to get formated data for esipy security"""
        return {'access_token': self.access_token,
                'refresh_token': self.refresh_token,
                'expires_in': (
                    self.access_token_expires - datetime.utcnow()
                ).total_seconds}

    def update_token(self, token_response):
         """ helper function to update token data from SSO response """
         self.access_token = token_response['access_token']
         self.access_token_expires = datetime.fromtimestamp(time.time() + token_response['expires_in'])
         if 'refresh_token' in token_response:
            self.refresh_token = token_response['refresh_token']

    def __repr__(self):
        return '<Char %r>' % self.character_name