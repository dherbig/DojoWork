from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/results', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   # redirects back to the '/' route
   #BEST PRACTICE: Always redirect after handling POST data to avoid data being handled more than once!
   return render_template('/results.html', name=name, location=location, language=language, comment=comment)

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')
app.run(debug=True) # run our server
