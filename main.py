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
    recieve_TW = db.Column(db.Integer)
    recieve_CHN = db.Column(db.Integer)
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
        order_US = int(request.form['order_US'] or 0)
        order_TW = int(request.form['order_TW'] or 0)
        order_CHN = 0
        
        recieve_US = order_US
        recieve_TW = round(order_TW*0.8)
        recieve_CHN = 0

        inventory = max(0, recieve_US + recieve_TW - 453)
        dem_cov = min(453, recieve_US + recieve_TW)
        service_level = min(100,round(((recieve_US + recieve_TW)/453)*100))
        
        revenue = min(recieve_US+recieve_TW, 453)*200
        purchase = (order_US*100) + (order_TW*85)
        holding = inventory * 15

        profit = revenue - purchase - holding

        my_data = Data(order_US, order_TW, order_CHN, recieve_US, recieve_TW, recieve_CHN, inventory, profit)
        db.session.add(my_data)
        db.session.commit()
        
        return render_template("round1_feedback.html", content = "testing",
        order_US=order_US, order_TW=order_TW, recieve_US=recieve_US, recieve_TW=recieve_TW,
        inventory=inventory, dem_cov=dem_cov, service_level=service_level, profit=format(profit, ",.2f"))
    else:
        return render_template("round1.html", content = "testing")


@app.route('/round2/', methods=['GET', 'POST'])
def round2():

    if request.method == 'POST':
        return render_template("round2.html", content = "testing")
    else:
        return render_template("round2.html", content = "testing")


@app.route('/round3/', methods=['GET', 'POST'])
def round3():

    if request.method == 'POST':
        return render_template("round3.html", content = "testing")
    else:
        return render_template("round3.html", content = "testing")


@app.route('/round4/', methods=['GET', 'POST'])
def round4():

    if request.method == 'POST':
        return render_template("round4.html", content = "testing")
    else:
        return render_template("round4.html", content = "testing")


@app.route('/round5/', methods=['GET', 'POST'])
def round5():

    if request.method == 'POST':
        return render_template("round5.html", content = "testing")
    else:
        return render_template("round5.html", content = "testing")


@app.route('/round6/', methods=['GET', 'POST'])
def round6():

    if request.method == 'POST':
        return render_template("round6.html", content = "testing")
    else:
        return render_template("round6.html", content = "testing")

@app.route('/round7/', methods=['GET', 'POST'])
def round7():

    if request.method == 'POST':
        return render_template("round7.html", content = "testing")
    else:
        return render_template("round7.html", content = "testing")


@app.route('/round8/', methods=['GET', 'POST'])
def round8():

    if request.method == 'POST':
        return render_template("round8.html", content = "testing")
    else:
        return render_template("round8.html", content = "testing")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

app.run()