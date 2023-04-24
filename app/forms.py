from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Optional


class ExampleForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(message="Поле не должно быть пустым")])
    text = TextAreaField('Отзыв', validators=[DataRequired(message="Поле не должно быть пустым")])
    email = EmailField('Email', validators=[Optional()])
    rating = SelectField('Оценка', choices=[1, 2, 3, 4, 5])
    submit = SubmitField('Отправить')


class NewsForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(message="Поле не должно быть пустым")])
    text = TextAreaField('Текст новости', validators=[DataRequired(message="Поле не должно быть пустым")])
    submit = SubmitField('Добавить новость')
