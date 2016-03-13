#Main file that renders html templates
from flask import Flask, url_for, session, request, render_template, redirect, send_file# pragma: no cover
from app import app# pragma: no cover
from datetime import datetime, timedelta# pragma: no cover
from random import randrange# pragma: no cover
from flask_mail import Mail# pragma: no cover
import os # pragma: no cover
import json # pragma: no cover
import requests # pragma: no cover
from db_interaction import DbInteraction# pragma: no cover
from forms import LoginForm, AdminForm
from werkzeug.security import generate_password_hash, \
     check_password_hash
import requests
from logins import *


connect = DbInteraction("my_site_login", "abc123", "localhost", "my_site") # pragma: no cover

@app.route('/', methods=['GET'])# pragma: no cover
def home():

    return render_template("about.html")

@app.route('/about', methods=['GET'])
def about():

    return render_template("about.html")

@app.route('/projects', methods=['GET'])
def projects():

    return render_template("projects.html")

@app.route('/blog', methods=['GET'])
def blog():

    return render_template("blog.html")

@app.route('/contact', methods=['GET'])
def contact():

    return render_template("contact.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = LoginForm(request.form)
    if request.method == 'GET':
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
    form = AdminForm(request.form)
    if request.method == 'GET':
        technologies = connect.technology_choices()
        choices = []
        for i in technologies:
            print "name: ", i.name
            choices.extend([(i.value, i.name)])
        choices.extend([('other', 'Other')])
        form.technology.choices = choices
        return render_template("admin_home.html", form = form)

    title = form.title.data
    technology = form.technology.data
    if technology == "other":
       technology = form.other_technology.data
       image = form.image.data
       connect.add_new_technology(technology, image)




