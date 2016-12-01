#Main file that renders html templates
from flask import Flask, url_for, session, request, render_template, redirect, send_file, jsonify, json# pragma: no cover
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
import json

UPLOAD_FOLDER = './static/logos'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
slack_webhook = 'https://hooks.slack.com/services/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'
connect = DbInteraction() # pragma: no cover
# connect = DbInteraction("site_admin", "3qDMkSQcQt2wZuUT", "my-site-rds-db.cyiv51njreag.eu-west-1.rds.amazonaws.com:3306", "my_site_db")

@app.route('/', methods=['GET'])# pragma: no cover
@app.route('/home', methods=['GET'])# pragma: no cover
def home():
    session['logged_in'] = False
    return render_template("index.html")

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    form = ProjectForm(request.form)
    list_of_projects = connect.project()
    if request.method == 'GET':
        if session['logged_in']:
            return render_template("projects.html", list_of_projects = list_of_projects, admin = True)
        else:
            return render_template("projects.html", list_of_projects = list_of_projects)
    project_dict = json.loads(request.data)
    if "data-hover" in project_dict:
        connect.add_project_tracking(project_dict["data-hover"], "hover")
    elif "data-click-git" in project_dict:
        connect.add_project_tracking(project_dict["data-click-git"], "click-git")
    elif "data-click-youtube" in project_dict:
        connect.add_project_tracking(project_dict["data-click-youtube"], "click-youtube")
    return "Post successful"

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")

    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")
    print name
    slack_notification_payload={"text": "New Message- \n\nName: {0} \nEmail: {1} \nPhone: {2} \nMessage: \n{3}".format(name, email, phone, message)}
    requests.post(slack_webhook, data=json.dumps(slack_notification_payload))
    return render_template("contact.html", message="Thanks for getting in touch :)")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = UserForm(request.form)
    if request.method == 'GET':
        session['logged_in'] = False
        return render_template("admin_login.html", form = form)

    username = form.username.data
    password = form.password.data
    user = connect.get_user(username)
    if user:
        generate_password_hash(password)
        print user.password
        correct_login = check_password_hash(user.password, password)
        if correct_login:

            session['logged_in'] = True

            return redirect(url_for('admin_home'))
        else:
            error = "Incorrect username or password"
    else:
        error = "Incorrect username or password"
    return render_template("admin_login.html", form = form, error = error)

@app.route('/add_project', methods=['GET', 'POST'])
@login_required
def admin_home():
    form = ProjectForm(request.form)
    if request.method == 'GET':
        project = None
        if request.args.get('id'):
            project_id = request.args.get('id')
            project = connect.project(project_id)
            form.title.data = project.title
            form.description.data = project.description
            form.url.data = project.url
            form.youtube.data = project.youtube
        return render_template("admin_home.html", form = form)

    elif request.method == 'POST':
        project_id = request.args.get('id')
        title = form.title.data
        timestamp = datetime.datetime.now()
        category = form.category.data
        technology = form.technology.data
        if technology.name == "Other":
           new_technology = form.other_technology.data
           print new_technology
           image_name = request.files[form.image.name]
           filename = secure_filename(image_name.filename)
           filepath = app.config['UPLOAD_FOLDER'] + "/" + filename
           #image_name.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           image_name.save(os.path.join(app.root_path, './static/logos', filename))
           connect.add_new_technology(new_technology, filepath)
           technology = connect.get_technology(new_technology)

        description = form.description.data
        url = form.url.data
        youtube = form.youtube.data
        if project_id:
             connect.update_project(project_id, title, category.id, technology.id, description, url, youtube)
        else:
            connect.add_project(title, category.id, technology.id, description, url, youtube)

        return redirect(url_for('projects'))

@app.route('/hobbies', methods=['GET'])
def hobbies():
    return render_template("hobbies.html")

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    if request.method == 'GET':
        session['logged_in'] = False
        return redirect(url_for('about'))



