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
from forms import LoginForm
from password_encryption import Authentication
import requests


# connect = DbInteraction("my_site_login", "abc123", "localhost", "my_site") # pragma: no cover

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
    authenticate_login = Authentication(username, password)
    print authenticate_login.pw_hash
    check_user = connect.check_login(username, authenticate_login.pw_hash)
    if check_user:
        error = "Successful login"

    else:
        error = "User not found"
    return render_template("admin_login.html", form = form, error = error)




