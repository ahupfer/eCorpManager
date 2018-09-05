from app import db, login_manager

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)

    @login_manager.user_loader
    def load_user(self, user_id):
        return User.get(user_id)

    def __repr__(self):
        return '<User %r>' % self.username
