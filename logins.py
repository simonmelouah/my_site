#User logins and sessions
from flask import Flask, url_for, redirect
import views
from functools import wraps

def login_required(test):
    
    @wraps(test)
    def wrap(*args, **kwargs):
        # if views.session['logged_in'] == True:
        if views.session.get('logged_in'):
            return test(*args, **kwargs)
        else:
            return redirect(url_for('home'))
    return wrap
