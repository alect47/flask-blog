from flask_wtf import FlaskFormgit
from wtforms import StringField

class RegistrationForm(FlaskForm):
    username = StringField('Username')
