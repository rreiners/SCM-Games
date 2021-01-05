import os 
from flask import Flask, request, render_template, render_template_string, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

template_dir = os.path.abspath('./templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'games'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    round_id = db.Column(db.Integer, primary_key=True)
    order_US = db.Column(db.Integer)
    order_TW = db.Column(db.Integer)
    order_CHN = db.Column(db.Integer)
    recieve_US = db.Column(db.Integer)
    recieve_US = db.Column(db.Integer)
    recieve_US = db.Column(db.Integer)
    inventory = db.Column(db.Integer)
    profit = db.Column(db.Integer)

    def __init__(self, order_US, order_TW, order_CHN, recieve_US, recieve_TW, recieve_CHN, inventory, profit):
        self.order_US = order_US
        self.order_TW = order_TW
        self.order_CHN = order_CHN
        self.recieve_US = recieve_US
        self.recieve_TW = recieve_TW
        self.recieve_CHN = recieve_CHN
        self.inventory = inventory
        self.profit = profit

@app.route('/')                
def home():
    
    return render_template("home.html", content = "testing")

@app.route('/round1/', methods=['GET', 'POST'])
def round1():

    if request.method == 'POST':
        order_US = int(request.form['order_US'])
        order_TW = int(request.form['order_TW'])
        order_CHN = 0
        
        recieve_US = order_1
        recieve_TW = round(order_TW*0.8)
        recieve_CHN = 0

        inventory = min(0, 453 - order_US - order_TW)
        
        revenue = min(order_US+order_TW, 0)*200
        purchase = (order_US*100) + (order_TW*85)
        holding = inventory * 15

        profit = revenue - purchase - holding

        my_data = Data(order_US, order_TW, order_CHN, recieve_US, recieve_TW, recieve_CHN, inventory, profit)
        db.session.add(my_data)
        db.session.commit()
        
        return render_template("round1_feedback.html", content = "testing",
        order_1=order_1, order_2=order_2, recieved_1=recieved_1, recieved_2=recieved_2,
        inventory=inventory)
    else:
        return render_template("round1.html", content = "testing")



"""@app.route('/round1/feedback/', methods=['GET', 'POST'])
def round1_feedback():

    if request.method == 'POST':
        return render_template("round1_feedback.html", content = "testing")
    else:
        return render_template("round1_feedback.html", content = "testing")"""


@app.route('/round2/', methods=['GET', 'POST'])
def round2():

    if request.method == 'POST':
        return render_template("round2.html", content = "testing")
    else:
        return render_template("round2.html", content = "testing")

@app.route('/round2/feedback/', methods=['GET', 'POST'])
def round2_feedback():

    if request.method == 'POST':
        return render_template("round2_feedback.html", content = "testing")
    else:
        return render_template("round2_feedback.html", content = "testing")


@app.route('/round3/', methods=['GET', 'POST'])
def round3():

    if request.method == 'POST':
        return render_template("round3.html", content = "testing")
    else:
        return render_template("round3.html", content = "testing")

@app.route('/round3/feedback/', methods=['GET', 'POST'])
def round3_feedback():

    if request.method == 'POST':
        return render_template("round3_feedback.html", content = "testing")
    else:
        return render_template("round3_feedback.html", content = "testing")

@app.route('/round4/', methods=['GET', 'POST'])
def round4():

    if request.method == 'POST':
        return render_template("round4.html", content = "testing")
    else:
        return render_template("round4.html", content = "testing")

@app.route('/round4/feedback/', methods=['GET', 'POST'])
def round4_feedback():

    if request.method == 'POST':
        return render_template("round4_feedback.html", content = "testing")
    else:
        return render_template("round4_feedback.html", content = "testing")

@app.route('/round5/', methods=['GET', 'POST'])
def round5():

    if request.method == 'POST':
        return render_template("round5.html", content = "testing")
    else:
        return render_template("round5.html", content = "testing")

@app.route('/round5/feedback/', methods=['GET', 'POST'])
def round5_feedback():

    if request.method == 'POST':
        return render_template("round5_feedback.html", content = "testing")
    else:
        return render_template("round5_feedback.html", content = "testing")

@app.route('/round6/', methods=['GET', 'POST'])
def round6():

    if request.method == 'POST':
        return render_template("round6.html", content = "testing")
    else:
        return render_template("round6.html", content = "testing")

@app.route('/round6/feedback/', methods=['GET', 'POST'])
def round6_feedback():

    if request.method == 'POST':
        return render_template("round6_feedback.html", content = "testing")
    else:
        return render_template("round6_feedback.html", content = "testing")

@app.route('/round7/', methods=['GET', 'POST'])
def round7():

    if request.method == 'POST':
        return render_template("round7.html", content = "testing")
    else:
        return render_template("round7.html", content = "testing")

@app.route('/round7/feedback/', methods=['GET', 'POST'])
def round7_feedback():

    if request.method == 'POST':
        return render_template("round7_feedback.html", content = "testing")
    else:
        return render_template("round7_feedback.html", content = "testing")

@app.route('/round8/', methods=['GET', 'POST'])
def round8():

    if request.method == 'POST':
        return render_template("round8.html", content = "testing")
    else:
        return render_template("round8.html", content = "testing")

@app.route('/round8/feedback/', methods=['GET', 'POST'])
def round8_feedback():

    if request.method == 'POST':
        return render_template("round8_feedback.html", content = "testing")
    else:
        return render_template("round8_feedback.html", content = "testing")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

app.run()