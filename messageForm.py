import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange, InputRequired, Regexp, Length


class MessageForm(FlaskForm):
    email = StringField("Email: ", validators=[Email(), InputRequired()])
    name = StringField("Name: ", validators=[DataRequired(), Regexp('[A-ZА-Я][a-zа-я]+'), Length(min=2, max=100)])
    password = StringField("password: ", validators=[DataRequired(), Regexp('(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'),
                                                     Length(min=8, max=100)])
    submit = SubmitField("Submit")