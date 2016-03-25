from wtforms import *
from wtforms.widgets import TextArea
# from flask_wtf import Form
# from flask_wtf.file import FileField

class Login(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=4, max=35), validators.DataRequired()])

class Admin(Form):
    title = StringField('Title', [validators.Length(min=4, max=25), validators.DataRequired()])
    category = SelectField('Category')
    technology = SelectField('Technology')
    other_technology = StringField('Other', [validators.Length(min=4, max=25), validators.DataRequired()])
    image = FileField('Image')
    description = StringField('Description', widget=TextArea())
    url = StringField('Url')
    youtube = StringField('Youtube')

class Project(Form):
    order_by_date = SelectField('Date_Order', [('Most Recent', 'Most Recent'), ('Oldest', 'Oldest')])
    category = SelectField('Category')
    technology = SelectField('Technology')

