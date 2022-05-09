from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from music_app.models import Playlist, Song, User
from music_app.login.forms import SignUpForm, LoginForm
from music_app.extensions import app, db, bcrypt


auth = Blueprint('auth', __name__)

# sign-up
@auth.route('/signup', methods=['GET', 'POST'])

