from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    # define your query
    query = "SELECT * FROM friends"
    # run query with query_db()
    friends = mysql.query_db(query)
    # pass data to our template
    return render_template('index.html', all_friends=friends)

#This handles the creation of a new friend
@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

#Deletes the friend with the passed ID
@app.route('/friends/<friend_id>/delete', methods=['POST'])
def destroy(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

#display the edit page for a friend
@app.route('/friends/<friend_id>/edit', methods=["GET"])
def edit(friend_id):
    # define your query
    query = "SELECT * FROM friends WHERE id=" + friend_id
    # run query with query_db()
    friend = mysql.query_db(query)
    return render_template('edit.html', friend=friend[0])

#Update the friend
@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    #The update query
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {
    'first_name': request.form['first_name'], 'last_name':  request.form['last_name'], 'occupation': request.form['occupation'], 'id': friend_id
    }
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return redirect('/')

app.run(debug=True)
