from flask import Flask, render_template
app = Flask(__name__)

#GET route for root defined
@app.route('/')

#Function that runs when '/' (root) is the URL requested
def hello_world():
    return render_template('index.html', name='Brisela, Voice of Nightmares')

#GET route for '/success' (localhost:5000/success)
@app.route('/success')

#Function that runs when '/success' is requested
def success():
    #serve 'success.html'
    return render_template('success.html')
app.run(debug=True)

#The generic structure of an HTTP GET route that serves a new page is:
'''
@app.route('/some_route')
def some_function_name():
  // your code here
'''
#NOTE: function must IMMEDIATELY follow the .route!!!
