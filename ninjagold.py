from flask import Flask, render_template , redirect, session, request # Import Flask to allow us to create our app.
import random
app = Flask(__name__)    
                         
app.secret_key = "SecretKey"

@app.route('/')                                                   
def index():
    try:
        session['yourGold']
    except:
        session['yourGold'] = 0
        session['Update'] = 'You have no money'
    return render_template('index.html') 

@app.route('/process', methods=['POST'])
def process():
    if request.form['building'] == 'farm':
        val = random.randrange(10,20)
        print val
        session['yourGold'] += val
        print 'Farm'
    elif request.form['building'] == 'cave':
        val = random.randrange(5,10)
        print val
        session['yourGold'] += val
        print 'Cave'
    elif request.form['building'] == 'house':
        val = random.randrange(2,5)
        print val
        session['yourGold'] += val
        print 'House'
    elif request.form['building'] == 'casino':
        i = random.randrange(0,1)
        print i
        if i:
            val = random.randrange(0,50)
            print val
            session['yourGold'] += val
        else:
            val = random.randrange(0,50)
            print val
            session['yourGold'] -= val
        print 'Casino'    
    return redirect('/')

app.run(debug=True)      # Run the app in debug mode.
