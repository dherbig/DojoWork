from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'emailCollector')
app.secret_key = 'meowmeowmeow'
EMAIL_REGEX = re.compile(r'^[a-xA-Z0-9.+_-]+@[a-xA-Z0-9.+_-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addEmail', methods=['POST'])
def collect():
    error = 0
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        error += 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address')
        error += 1
    else:
        flash("The email address you entered, " + request.form['email'] + " is a VALID email address! Thank you!")

    query = "INSERT INTO emails (email, created_at, modified_at) VALUES (:email, NOW(), NOW())"
    data = {
        'email': request.form['email']
    }
    if error < 1:
        mysql.query_db(query, data)
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/success')
def horray():
        query2 = "SELECT * FROM emails"
        emails = mysql.query_db(query2)
        return render_template('success.html', lastEmail = mysql.query_db('SELECT email FROM emails ORDER BY email DESC LIMIT 1;')[0]['email'], emailList = emails)
app.run(debug=True)
