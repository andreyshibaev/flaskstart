from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



class contactForm(FlaskForm):
    name = StringField()
    email = StringField()
    message = StringField()
    submit = SubmitField()