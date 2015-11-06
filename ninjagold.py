from flask import Flask, render_template , redirect, session, request # Import Flask to allow us to create our app.
import random
import time
import datetime
app = Flask(__name__)    
                         
app.secret_key = "SecretKey"

@app.route('/')                                                   
def index():
    try:
        session['yourGold']
        session['fromWhere'] = ''
        session['update'] = 0
    except:
        session['yourGold'] = 0
        session['fromWhere'] = ''
        session['update'] = 0
    return render_template('index.html') 

@app.route('/process', methods=['POST'])
def process():
    if request.form['building'] == 'farm':
        val = random.randrange(10,20)
        session['update'] = val
        session['yourGold'] += val
        session['fromWhere'] ='Farm'
    elif request.form['building'] == 'cave':
        val = random.randrange(5,10)
        session['update'] = val
        session['yourGold'] += val
        session['fromWhere'] ='Cave'
    elif request.form['building'] == 'house':
        val = random.randrange(2,5)
        print val
        session['yourGold'] += val
        session['fromWhere'] ='House'
    elif request.form['building'] == 'casino':
        i = random.randrange(0,1)
        print i
        if i:
            val = random.randrange(0,50)
            session['update'] = val
            session['yourGold'] += val
        else:
            val = random.randrange(0,50)
            session['update'] = -1 * val
            session['yourGold'] -= val
        session['fromWhere'] ='Casino'    

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print st

    return redirect('/')

app.run(debug=True)      # Run the app in debug mode.
