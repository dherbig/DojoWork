from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def countRefresh(num):
    try:
        if (num>-1):
            session['counter'] += num
        else:
            session['counter'] = 0
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():
    countRefresh(1)
    return render_template("index.html")

@app.route('/poke', methods=['POST'])
def poke():
    if (request.form['poke'] == '2'):
        countRefresh(int(request.form['poke']))
    else:
        countRefresh(-1)
    return redirect(url_for('index'))
app.run(debug=True)
