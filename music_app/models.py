from sqlalchemy_utils import URLType
from music_app.extensions import db
from music_app.utils import FormEnum
from flask_login import UserMixin


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), nullable=False, unique=True)
  password = db.Column(db.String(80), nullable=False)


class Genre(FormEnum):
  UNKNOWN = 'Unknown'
  HIPHOP = 'Hip Hop'
  POP = 'Pop'
  RAP = 'Rap'
  TRAP = 'Trap'
  COUNTRY = 'Country'
  JAZZ = 'Jazz'
  ROCK = 'Rock'


class Playlist(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), nullable=False)
  genre = db.Column(db.Enum(Genre), default=Genre.UNKNOWN)
  songs = db.relationship('Song', back_populates='playlist')


class Song(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  artist = db.Column(db.String(80), nullable=False)
  photo_url = db.Column(URLType)
  playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
  playlist = db.relationship('Playlist', back_populates='songs')
