from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from music_app.models import Playlist, Song, User
from music_app.auth.forms import SignUpForm, LoginForm
from music_app.extensions import app, db, bcrypt


auth = Blueprint('auth', __name__)

# sign-up
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignUpForm()

  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(
      username=form.username.data,
      password=hashed_password
    )
    db.session.add(user)
    db.session.commit()
    flash('Successfully Created Account.', 'success')
    return redirect(url_for('auth.login'))
  return render_template('signup.html', form=form)
  

@auth.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=True)
      next_page = request.args.get('next')
      flash('Successfully Logged In.', 'success')
      return redirect(next_page if next_page else url_for("main.home"))
  return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  flash('Successfully Logged Out!', 'success')
  return redirect(url_for('main.home'))