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
        session['fromWhere']
        session['update']
        session['timeStamp']
        session['activities']
    except:
        session['yourGold'] = 0
        session['fromWhere'] = ''
        session['update'] = 0
        session['timeStamp'] = ''
        session['activities'] = ['Start']
    return render_template('index.html') 

@app.route('/process', methods=['POST'])
def process():
    
    if request.form['building'] == 'farm':
        val = random.randrange(10,20)
        session['update'] = val
        session['yourGold'] += val
        session['fromWhere'] ='farm'
    elif request.form['building'] == 'cave':
        val = random.randrange(5,10)
        session['update'] = val
        session['yourGold'] += val
        session['fromWhere'] ='cave'
    elif request.form['building'] == 'house':
        val = random.randrange(2,5)
        print val
        session['yourGold'] += val
        session['fromWhere'] ='house'
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
        session['fromWhere'] ='casino'    

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    session['timeStamp']  = st
    
    actv = ''
    if  session['fromWhere'] == 'farm' or session['fromWhere'] == 'cave' or  session['fromWhere'] == 'house':            
        actv = 'Earned' + str(session['update']) + 'gold from ' + session['fromWhere'] + '!' +  session['timeStamp']        
    else:
        actv = 'Entered a casino and lost ' + str(session['update']) + ' gold ... Ouch... ' + session['timeStamp']        
    
    session['activities'].append(actv)


    return redirect('/')

app.run(debug=True)      # Run the app in debug mode.
