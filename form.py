from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ExampleForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    submit = SubmitField('Отправить')
