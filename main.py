import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a217830a53e658f01c87b204d83e8f6c9675'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():   
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = ''
    return render_template("register.html", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/404.html'), 404