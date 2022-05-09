from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from music_app.models import Genre, Playlist, Song


class PlaylistForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  genre = SelectField('Genre', choices=Genre.choices(), validators=[DataRequired()])
  submit = SubmitField('Submit')

class SongForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  artist = StringField('Artist', validators=[DataRequired()])
  photo_url = StringField('Photo URL', validators=[DataRequired()])
  playlist = QuerySelectField('Playlist', query_factory=lambda: Playlist.query, validators=[DataRequired()])
  submit = SubmitField('Submit')
