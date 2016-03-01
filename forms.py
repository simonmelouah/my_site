from wtforms import Form, BooleanField, PasswordField, validators, StringField

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=4, max=35), validators.DataRequired()])

