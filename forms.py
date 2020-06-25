from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, AnyOf, NumberRange


class LuckyForm(FlaskForm):
    """ Form for lucky number project """

    name = StringField('Name', validators=[InputRequired(message='This field is required')])
    year = IntegerField('Birth Year', validators=[
                        InputRequired(message='Invalid value. Year must be between 1900 and 2000'), NumberRange(min=1900, max=2000)])
    email = StringField('Email', validators=[InputRequired(message='This field is required')])
    color = StringField('Color', validators=[
                        InputRequired(message='Invalid value. Color must be one of "red", "green", "orange", "blue"'), AnyOf(['red', 'blue', 'green', 'orange'])])