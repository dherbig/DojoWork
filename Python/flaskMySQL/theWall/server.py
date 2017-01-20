from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
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
        password=request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)
        insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
        }
        mysql.query_db(insert_query, data)
        flash ('Success! Added to database', 'Success')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    query = 'SELECT email, password, first_name, last_name, id FROM users WHERE email=:email'
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    print ('The user provided data was ' + str(data))
    try:
        result = mysql.query_db(query, data)[0]
        print ('result was ' + str(result))
    except IndexError:
        flash('No such account!', 'Typo')
        return redirect('/')

    if bcrypt.check_password_hash(result['password'], data['password']):
        flash('Credentials verified. Welcome!')
        session['user'] = result['first_name'] + ' ' + result['last_name']
        session['userID'] = result['id']
    else:
        flash('Wrong password.  Try again.')
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/wall')
def scaleThe():
    query = "SELECT messages.id, messages.message, messages.created_at, messages.updated_at, users.first_name, users.last_name, messages.user_id FROM messages JOIN users on users.id = messages.user_id ORDER BY messages.created_at DESC"
    all_messages = mysql.query_db(query)
    query = "SELECT comments.id, comments.message_id, comments.comment, comments.created_at, comments.updated_at, users.first_name, users.last_name, comments.user_id FROM comments JOIN users on users.id = comments.user_id"
    all_comments = mysql.query_db(query)
    return render_template('wall.html', messageLog = all_messages, commentLog = all_comments)

@app.route('/newPost', methods=['POST'])
def message():
    print request.form
    print session
    query = "INSERT into messages (message, user_id, created_at, updated_at) VALUES (:content, :user_id, NOW(), NOW())"
    values = {
        "content": request.form['content'],
        "user_id": session['userID']
    }
    mysql.query_db(query, values)
    flash('Message Added!')
    return redirect('/wall')

@app.route('/postComment/<message_id>', methods=['POST'])
def comment(message_id):
    query = "INSERT into comments (comment, user_id, message_id, created_at, updated_at) VALUES (:content, :user_id, :message_id, NOW(), NOW())"
    values = {
        "content": request.form['comment'],
        "user_id": session['userID'],
        "message_id": message_id
    }
    mysql.query_db(query, values)
    flash('Comment posted!')
    return redirect('/wall')

@app.route('/delete/<postType>/<ident>')
def delete(postType, ident):
    print (postType + ' ' + ident)
    query = "DELETE FROM `" + postType + "s` WHERE `id` = '" + ident + "'"
    mysql.query_db(query)
    flash('Deleted your ' + postType)
    return redirect('/wall')

app.run(debug=True)