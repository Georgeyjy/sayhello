from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from sayhello import views, errors, commands
