from flask import render_template, redirect

from .forms import ExampleForm, NewsForm
from .models import Category, News, Feedback
from . import app, db


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
        feedback = Feedback()
        feedback.name = form.name.data
        feedback.text = form.text.data
        feedback.email = form.email.data
        feedback.rating = form.rating.data
        db.session.add(feedback)
        db.session.commit()
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