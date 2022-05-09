from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from music_app.extensions import app, db
from music_app.models import User, Genre, Playlist, Song
from music_app.main.forms import PlaylistForm, SongForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
  all_playlists = Playlist.query.all()
  return render_template('home.html', all_playlists=all_playlists)

# ---------------------------------------------------------------------------------
# playlist routes

@main.route('/new_playlist', methods=['GET', 'POST'])
def new_playlist():
  form = PlaylistForm()

  if form.validate_on_submit():
    new_playlist = Playlist(
      title = request.form.get('title'),
      genre = request.form.get('genre')
    )
    db.session.add(new_playlist)
    db.session.commit()
    flash('Successfully Created Playlist.')
    return redirect(url_for('main.playlist_details', playlist_id=new_playlist.id))
  return render_template('new_playlist.html', form=form)


@main.route('/playlist/<playlist_id>', methods=['GET', 'POST'])
def playlist_details(playlist_id):
  playlist = Playlist.query.get(playlist_id)
  form = PlaylistForm(obj=playlist)

  if form.validate_on_submit():
    playlist.title = form.title.data
    playlist.genre = form.genre.data

    db.session.add(playlist)
    db.session.commit()
    flash('Successfully Updated Playlist!')
    return redirect(url_for('main.playlist_details', playlist_id=playlist.id))

  return render_template('playlist_details.html', playlist=playlist, form=form)

# -------------------------------------------------------------------------------------------------
# song routes

@main.route('/new_song', methods=['GET', 'POST'])
def new_song():
  form = SongForm()

  if form.validate_on_submit():
    new_song = Song(
      name = form.name.data,
      artist = form.artist.data,
      photo_url = form.photo_url.data,
      playlist = form.playlist.data
    )
    db.session.add(new_song)
    db.session.commit()
    flash('Successfully Added a New Song.')
    return redirect(url_for('main.song_details'))

  return render_template('new_song.html', form=form)

@main.route('/song/<song_id>', methods=['GET', 'POST'])
def song_details(song_id):
  song = Song.query.get(song_id)
  form = SongForm(obj=song)

  if form.validate_on_submit():
    song.name = form.name.data
    song.artist = form.artist.data
    song.photo_url = form.photo_url.data
    song.playlist = form.playlist.data

    db.session.add(song)
    db.session.commit()
    flash('Successfully Updated Song.')
    return redirect(url_for('main.song_details', song_id=song.id))
  return render_template('song_details.html', song=song, form=form)
