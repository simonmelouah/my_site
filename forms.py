from wtforms import *
from wtforms.fields.html5 import EmailField, IntegerField
from flask_wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.widgets import TextArea
from models import *
from db_interaction import *

connect = DbInteraction()

UserFormBase = model_form(User, Form)
ProjectFormBase = model_form(Project, Form)

class UserForm(UserFormBase):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('', [validators.optional(), validators.DataRequired()])

class ProjectForm(ProjectFormBase):
    title = StringField('Title', [validators.Length(min=4, max=25), validators.DataRequired()])
    technology = QuerySelectField('Technology', query_factory= connect.technology_choices,
                        get_pk=lambda a: a.id,
                        get_label=lambda a: a.name, allow_blank=True, blank_text=u'Select a technology...')
    category = QuerySelectField('Category', query_factory= connect.category_choices,
                            get_pk=lambda a: a.id,
                            get_label=lambda a: a.name, allow_blank=True, blank_text=u'Select a category...')
    # technology = SelectField(u'Technology', choices=[("", "Select a technology...")])
    # category = SelectField(u'Category', choices = [("", "Select a category...")])
    other_technology = StringField('Other', [validators.Length(min=4, max=25), validators.DataRequired()])
    image = FileField('Image')
    description = StringField('Description', widget=TextArea())
    url = StringField('Url')
    youtube = StringField('Youtube')


