from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Optional

import os


class ExampleForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(message="Поле не должно быть пустым")])
    text = TextAreaField('Отзыв', validators=[DataRequired(message="Поле не должно быть пустым")])
    email = EmailField('Email', validators=[Optional()])
    rating = SelectField('Оценка', choices=[1, 2, 3, 4, 5])
    submit = SubmitField('Отправить')


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

context = '<h1>Заголовок!</h1>'


@app.route('/')
def start_page():
    return render_template("index.html")


@app.route('/news')
def new():
    return "Новости"


@app.route('/news_detail/<int:id>')
def news_detail(id):
    return render_template("news_detail.html")


@app.route('/category/<string:name>')
def category(name):
    return f"Категория: {name}"


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = ExampleForm()
    if form.validate_on_submit():
        name = form.name.data
        text = form.text.data
        email = form.email.data
        rating = form.rating.data
        print(name, text, email, rating)
        return redirect('/')
    return render_template("form.html", form=form)
