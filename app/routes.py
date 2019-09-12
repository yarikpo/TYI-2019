# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from flask import redirect
# import algo/main
from app.forms import LoginForm

@app.route('/check')
def check():
    # return redirect('/index')
    return render_template("check.html")

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    way = []
    if form.validate_on_submit():
        way = [[50, 50], [40, 40], [50, 40]]
        return render_template("index.html", form = form, info = way)
    return render_template("index.html", form = form, info = way)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/check')
    return render_template("login.html", form = form)

