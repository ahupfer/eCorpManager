from wtforms import Form, validators, StringField, PasswordField


class LoginForm(Form):
    email = StringField('eMail Address', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
    validators.DataRequired()])