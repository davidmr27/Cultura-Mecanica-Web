import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/404.html'), 404