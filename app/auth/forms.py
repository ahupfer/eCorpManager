from wtforms import Form, validators, StringField, PasswordField, SubmitField, ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('eMail Address', [validators.DataRequired('please enter a email address'),
                                          validators.email('his field requires a valid email address')])
    password = PasswordField('Password', [
    validators.DataRequired("please enter your password")])
    submit = SubmitField('Login')


class RegisterForm(Form):
    username = StringField ('Username', [validators.DataRequired()])
    email = StringField('email Address', [validators.DataRequired('please enter a email address'),
                                          validators.email('this field requires a valid email address')])
    password = PasswordField('Password', [validators.DataRequired()])
    password2 = PasswordField('Repeat Password', [validators.DataRequired(),
                                                  validators.EqualTo('password', message='Password must match!')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different unsername.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email.')





