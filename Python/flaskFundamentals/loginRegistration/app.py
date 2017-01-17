from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'login_reg')

app.secret_key = "superprotected"
EMAIL_REGEX = re.compile(r'^[a-xA-Z0-9.+_-]+@[a-xA-Z0-9.+_-]+\.[a-zA-Z]+$')

name = re.compile(r'^[a-zA-Z]')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    error = 0
    if len(request.form['first_name']) <2:
        error += 1
        flash("need more characters", 'Character Error')
    elif not name.match(request.form['first_name']):
        error += 1
        flash('no numbers allowed in name', 'Mismatch')

    if len(request.form['last_name']) <2:
        error += 1
        flash("need more characters", 'Character Error')
    elif not name.match(request.form['last_name']):
        error += 1
        flash('no numbers allowed in name', 'Mismatch')

    if not EMAIL_REGEX.match(request.form['email']):
        error += 1
        flash('email is not valid', 'formatting error')

    if len(request.form['password']) < 9:
        error += 1
        flash ('password needs to be 9 characters or more!', 'length error')

    if request.form['password'] != request.form['confirm']:
        error += 1
        flash ('passwords do not match!', 'Typo')
    if error == 0:
        flash('Thanks for submitting your information!')
    return redirect('/')

# @app.route('/login', methods=['POST'])
# def login():
#
app.run(debug=True)
