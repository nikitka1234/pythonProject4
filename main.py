from flask import Flask, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Optional

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os


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


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

context = '<h1>Заголовок!</h1>'


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route('/')
def start_page():
    news_list = News.query.all()
    return render_template("index.html", news=news_list)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news = News.query.get(id)
    return render_template("news_detail.html", news=news)


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


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        db.session.add(news)
        db.session.commit()
        return redirect('/')
    return render_template("add_news.html", form=form)
