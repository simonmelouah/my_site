#Main file that renders html templates
from flask import Flask, url_for, session, request, render_template, redirect, send_file# pragma: no cover
from app import app# pragma: no cover
import datetime
from db_interaction import DbInteraction# pragma: no cover
from forms import *
from werkzeug import secure_filename
from werkzeug.security import generate_password_hash, \
     check_password_hash
import requests
import os
from logins import *

UPLOAD_FOLDER = './static/logos'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# connect = DbInteraction("my_site_login", "abc123", "localhost", "my_site") # pragma: no cover

@app.route('/', methods=['GET'])# pragma: no cover
def home():
    return render_template("about.html")

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/projects', methods=['GET'])
def projects():
    form = Project(request.form)
    if request.method == 'GET':
        list_of_projects = connect.get_projects()
        if session['logged_in']:
            return render_template("projects.html", list_of_projects = list_of_projects, admin = True)
        else:
            return render_template("projects.html", list_of_projects = list_of_projects)

@app.route('/blog', methods=['GET'])
def blog():

    return render_template("blog.html")

@app.route('/contact', methods=['GET'])
def contact():

    return render_template("contact.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = Login(request.form)
    if request.method == 'GET':
        session['logged_in'] = False
        return render_template("admin_login.html", form = form)

    username = form.username.data
    password = form.password.data
    user = connect.get_user(username)
    if user:
        generate_password_hash(password)
        correct_login = check_password_hash(user.password, password)
        if correct_login:

            session['logged_in'] = True

            return redirect(url_for('admin_home'))
        else:
            error = "Incorrect username or password"
    else:
        error = "Incorrect username or password"
    return render_template("admin_login.html", form = form, error = error)

@app.route('/admin_home', methods=['GET', 'POST'])
@login_required
def admin_home():
    form = Admin(request.form)
    if request.method == 'GET':
        technologies = connect.technology_choices()
        categories = connect.category_choices()
        category_choices = []
        technology_choices = []
        for i in categories:
            category_choices.extend([(i.name, i.name)])
        for i in technologies:
            technology_choices.extend([(i.name, i.name)])
        form.category.choices = category_choices
        technology_choices.extend([('other', 'Other')])
        form.technology.choices = technology_choices
        return render_template("admin_home.html", form = form)

    title = form.title.data
    timestamp = datetime.datetime.now()
    category = form.category.data
    technology = form.technology.data
    if technology == "other":
       technology = form.other_technology.data
       image_name = request.files[form.image.name]
       filename = secure_filename(image_name.filename)
       filepath = app.config['UPLOAD_FOLDER'] + "/" + filename
       #image_name.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       image_name.save(os.path.join(app.root_path, './static/logos', filename))
       connect.add_new_technology(technology, filepath)

    description = form.description.data
    url = form.url.data
    youtube = form.youtube.data
    category_object = connect.get_category(category)
    technology_object = connect.get_technology(technology)
    connect.add_project(title, timestamp, category_object.id, technology_object.id, description, url, youtube)

    return redirect(url_for('projects'))

@app.route('/logout', methods=['GET'])
def logout():
    if request.method == 'GET':
        session['logged_in'] = False
        return redirect(url_for('about'))



