from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from music_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'secretkey'
db = SQLAlchemy(app)

###########################
# Authentication
###########################

login_manager = LoginManager()
login_manager.login_view = "auth.auth"
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

bcrypt = Bcrypt(app)



