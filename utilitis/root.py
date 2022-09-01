from flask import Flask, render_template, request, redirect
from models import User
from app import app, db


@app.route('/', methods=['get'])
def common():
    return render_template('choose.html')

@app.route('/add', methods=['Get'])
def index():
    return render_template('register.html')


@app.route('/input/register', methods=['post'])
def add_user():
    form = request.form
    a = User(first_name=form['first_name'], last_name=form['last_name'], Email=form['Email'], password=form['password'])
    db.session.add(a)
    db.session.commit()
    return a.serialize


@app.route('/check', methods=['get'])
def check():
    return render_template('authorization.html')


@app.route('/authorization', methods=['post'])
def authorization():
    form = request.form
    i = 0
    if User.query.filter_by(password=form['password']) and User.query.filter_by(Email=form['Email']):
        i = +1
    if i > 0:
        return 'hello'
    elif i == 0:
        return 'o da'

