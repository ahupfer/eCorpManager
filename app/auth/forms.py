from wtforms import Form, validators, StringField, PasswordField

#TODO: validators error do not shonw on the website

class LoginForm(Form):
    email = StringField('eMail Address', [validators.DataRequired("please enter a email address"
    ),
                                          validators.email("his field requires a valid email address")])
    password = PasswordField('Password', [
    validators.DataRequired("please enter your password")])