from flask import Flask, request, redirect, render_template, session
import datetime
import random
app = Flask(__name__)
app.secret_key = 'ninjasNeverTell!'
@app.route('/')
def index():
    if not 'wallet' in session:
        session['wallet'] = 0
    if not 'activityLog' in session:
        session['activityLog'] = ['Your actions will be recorded here... Do something!']
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def chaChing():
    building = request.form['building']
    spoils = 0
    color = 'green'
    logbook = ''
    #Is it a casino?
    #The casino track is seperate due to the differences in the
    #logbook syntax we use for it.
    if building == "casino":
        # Casino: +- 0-50
        #Grab a random number between -50 - 50
        spoils += random.randrange(-50, 50)
        logbook = 'Entered a casino and '
        if spoils < 0:
            color = 'red'
            logbook += 'lost ' + str(abs(spoils)) + ' gold... Ouch.'
        else:
            logbook += 'won ' + str(abs(spoils)) + ' gold.  Yay!'
            print str(spoils) + ' casino'
    else:
        if building == "cave":
            #Grab a random number between 5-10
            spoils += random.randrange(5, 10)
            print str(spoils) + " cave!"
        elif building == "house":
            #House: + 2-5
            #Grab a random number between 2-5
            spoils += random.randrange(2, 5)
            print str(spoils) + " house"
        elif building == "reset":
            session.clear()
            return redirect('/')
        else:
            #Grab a random number between 10-20
            spoils = random.randrange(10, 20)
            print str(spoils) + ' farm!'
        logbook = 'Earned ' + str(spoils) + ' gold from the ' + building + '!'

    #add the timestamp to the log
    logbook += ' ' + datetime.datetime.now().strftime('%Y/%m/%d %X')
    #add the change in amount to the wallet
    session['wallet']+=spoils
    #Add the action to the log
    session['activityLog'].append(logbook)

    return render_template("index.html")

app.run(debug=True)
