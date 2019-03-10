import flask
import os
app = flask.Flask(__name__)
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

from views import *
from db_interaction import *

app.secret_key = 'weojfriowejiorjweiirjoewrj'
if __name__ == '__main__':
    app.secret_key = 'weojfriowejiorjweiirjoewrj'
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
