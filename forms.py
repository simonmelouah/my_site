from wtforms import *
from wtforms.widgets import TextArea, FileInput

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=4, max=35), validators.DataRequired()])

class AdminForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=25), validators.DataRequired()])
    technology = SelectField('Technology')
    other_technology = StringField('Other', [validators.Length(min=4, max=25), validators.DataRequired()])
    image = StringField('Image', widget=FileInput())
    description = StringField('Description', widget=TextArea())
    url = StringField('Url', [validators.Length(min=4, max=500), validators.DataRequired()])

