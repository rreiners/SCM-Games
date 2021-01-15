from flask import Flask, request, render_template, render_template_string, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

## Notiz an Jana: wenn du an den HTML ansichten auf einem localen Server arbeiten möchtest, dann musst du 
## den app.secret_key auskommentieren und den string 'postgres://xjezuiuthzzkax:e66256fb0f46249a929c24c9ad581ff139a192ffa376536e152f948061afdc9f@ec2-54-216-202-161.eu-west-1.compute.amazonaws.com:5432/dbgg781qn34tnm'
## auskommentieren und mit 'sqlite:///users.sqlite3' ersetzten dfsd

app = Flask(__name__)
app.secret_key = '022fde4f6f0721b9ed817c5ae18edb54307600af64379f5120b5a1553f8bab52'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'#'postgres://xjezuiuthzzkax:e66256fb0f46249a929c24c9ad581ff139a192ffa376536e152f948061afdc9f@ec2-54-216-202-161.eu-west-1.compute.amazonaws.com:5432/dbgg781qn34tnm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

usedCN = False

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_US = db.Column(db.Integer)
    order_TW = db.Column(db.Integer)
    order_CHN = db.Column(db.Integer)
    receive_US = db.Column(db.Integer)
    receive_TW = db.Column(db.Integer)
    receive_CHN = db.Column(db.Integer)
    analysis = db.Column(db.Integer)
    measure1 = db.Column(db.Integer)
    measure2 = db.Column(db.Integer)
    measure3 = db.Column(db.Integer)
    inventory = db.Column(db.Integer)
    round_profit = db.Column(db.Integer)
    total_profit = db.Column(db.Integer)

    def __init__(self, order_US, order_TW, order_CHN, receive_US, receive_TW, receive_CHN, analysis, measure1, measure2, measure3, inventory, round_profit, total_profit):
        self.order_US = order_US
        self.order_TW = order_TW
        self.order_CHN = order_CHN
        self.receive_US = receive_US
        self.receive_TW = receive_TW
        self.receive_CHN = receive_CHN
        self.analysis = analysis
        self.measure1 = measure1
        self.measure2 = measure2
        self.measure3 = measure3
        self.inventory = inventory
        self.round_profit = round_profit
        self.total_profit = total_profit

@app.route('/')                
def home():
    
    #for i in range(1,11):
        #my_empty_data = Data(0,0,0,0,0,0,0,0,0,0,0,0,0)
        #db.session.add(my_empty_data)
        #db.session.commit()
    
    return render_template("home.html", content = "testing")

@app.route('/round1/', methods=['GET', 'POST'])
def round1():
   
    for i in range(1,11):    
        my_data = Data.query.get(i)
        my_data.order_US = 0
        my_data.order_TW = 0
        my_data.order_CHN = 0
        my_data.receive_US = 0
        my_data.receive_TW = 0
        my_data.receive_CHN = 0
        my_data.analysis = 0
        my_data.measure1 = 0
        my_data.measure2 = 0
        my_data.measure3 = 0
        my_data.inventory = 0
        my_data.round_profit = 0
        my_data.total_profit = 0
        db.session.commit()

    if request.method == 'POST':
        # get input values from inputform 
        order_US = int(request.form['order_US'] or 0)
        order_TW = int(request.form['order_TW'] or 0)
        order_CHN = 0
        
        # calculate whats happening 
        receive_US = order_US
        receive_TW = round(order_TW*0.8)
        receive_CHN = 0
        inventory = max(0, receive_US + receive_TW - 453)
        dem_cov = min(453, receive_US + receive_TW)
        service_level = min(100,round(((receive_US + receive_TW)/453)*100))
        revenue = min(receive_US+receive_TW, 453)*200
        purchase = (receive_US*100) + (receive_TW*85)
        holding = inventory * 15
        round_profit = revenue - purchase - holding
        total_profit = round_profit

        # access Database row 1 and update Database
        my_data = Data.query.get(1)
        my_data.order_US = order_US
        my_data.order_TW = order_TW
        my_data.order_CHN = order_CHN
        my_data.receive_US = receive_US
        my_data.receive_TW = receive_TW
        my_data.receive_CHN = receive_CHN
        my_data.inventory = inventory
        my_data.round_profit = round_profit
        my_data.total_profit = total_profit
        db.session.commit()
        
        return render_template("round1_feedback.html", content = "testing",
        order_US=order_US, order_TW=order_TW, receive_US=receive_US, receive_TW=receive_TW,
        inventory=inventory, dem_cov=dem_cov, service_level=service_level, profit=format(total_profit, ",.2f"))
    else:
        return render_template("round1.html", content = "testing")


@app.route('/round2/', methods=['GET', 'POST'])
def round2():

    if request.method == 'POST':
        # get inventory and profit from database
        query_profit = db.session.query(Data.total_profit).filter_by(id = 1).first()._asdict()
        query_inventory = db.session.query(Data.inventory).filter_by(id = 1).first()._asdict()
        profit_r1 = int(query_profit.get("total_profit"))
        inventory_r1 = int(query_inventory.get("inventory"))
        
        # get data from form 
        option1 = int(request.form.get('option1') or 0)
        option2 = int(request.form.get('option2') or 0)
        analysis = int(request.form['analysis_purchase'] or 0)
        order_US = int(request.form['order_US'] or 0)
        order_TW = int(request.form['order_TW'] or 0)
        order_CHN = 0 
        
        # calculate whats happening
        receive_CHN = 0
        receive_US = order_US
        if option1 == 13500:
            receive_TW = round(order_TW*0.8)
        else:
            receive_TW = round(order_TW*0.4) 
        if (option2 == 5000 and inventory_r1 + receive_US + receive_TW < 370): 
            delta1 = 370 - inventory_r1 - receive_US - receive_TW
            delta2 = order_TW - receive_TW
            compensation = (min(delta1, delta2))  * 57.5
        else: 
            compensation = 0
        inventory = max(0, inventory_r1 + receive_US + receive_TW - 370)
        dem_cov = min(370, inventory_r1 + receive_US + receive_TW)
        service_level = min(100,round(((dem_cov)/370)*100))
        revenue = min(dem_cov, 370)*200
        purchase = (receive_US*100) + (receive_TW*85)
        holding = inventory * 15
        round_profit = revenue + compensation - purchase - holding - analysis - option1 - option2
        total_profit = round_profit + profit_r1

        # access Database row 2 and update Database
        my_data = Data.query.get(2)
        my_data.order_US = order_US
        my_data.order_TW = order_TW
        my_data.order_CHN = order_CHN
        my_data.receive_US = receive_US
        my_data.receive_TW = receive_TW
        my_data.receive_CHN = receive_CHN
        my_data.analysis = analysis
        my_data.measure1 = option1
        my_data.measure2 = option2
        my_data.inventory = inventory
        my_data.round_profit = round_profit
        my_data.total_profit = total_profit
        db.session.commit()
        
        return render_template("round2_feedback.html", content = "testing", 
        order_US=order_US, order_TW=order_TW, receive_US=receive_US, receive_TW=receive_TW, compensation=format(compensation, ",.2f"),
        inventory=inventory, dem_cov=dem_cov, service_level=service_level, round_profit=format(round_profit, ",.2f"), total_profit=format(total_profit, ",.2f"))
    else:
        query_profit = db.session.query(Data.total_profit).filter_by(id = 1).first()._asdict()
        query_inventory = db.session.query(Data.inventory).filter_by(id = 1).first()._asdict()
        profit_r1 = query_profit.get("total_profit")
        inventory_r1 = query_inventory.get("inventory")
        
        return render_template("round2.html", content = "testing", 
        profit_r1 = profit_r1, inventory_r1 = inventory_r1)


@app.route('/round3/', methods=['GET', 'POST'])
def round3():
    global usedCN
    if request.method == 'POST':
        # get inventory and profit from database
        query_profit = db.session.query(Data.total_profit).filter_by(id = 2).first()._asdict()
        query_inventory = db.session.query(Data.inventory).filter_by(id = 2).first()._asdict()
        profit_r2 = int(query_profit.get("total_profit"))
        inventory_r2 = int(query_inventory.get("inventory"))
        
        # get data from form 
        option1 = int(request.form.get('option1') or 0)
        option2 = int(request.form.get('option2') or 0)
        analysis = int(request.form['analysis_purchase'] or 0)
        order_US = int(request.form['order_US'] or 0)
        order_TW = int(request.form['order_TW'] or 0)
        order_CHN = int(request.form['order_CN'] or 0)
        
        if option1 != 0:
            usedCN = True
        
        
        # calculate whats happening
        receive_CHN = order_CHN
        receive_US = order_US
        receive_TW = order_TW
        inventory = max(0, inventory_r2 + receive_US + receive_TW + receive_CHN - 480)
        dem_cov = min(480, inventory_r2 + receive_US + receive_TW + receive_CHN)
        service_level = min(100,round(((dem_cov)/480)*100))
        revenue = min(dem_cov, 480)*200
        purchase = (receive_US*100) + (receive_TW*85)+ (receive_CHN*90)
        holding = inventory * 15
        round_profit = revenue - purchase - holding - analysis - option1 - option2
        total_profit = round_profit + profit_r2

        # access Database row 3 and update Database
        my_data = Data.query.get(3)
        my_data.order_US = order_US
        my_data.order_TW = order_TW
        my_data.order_CHN = order_CHN
        my_data.receive_US = receive_US
        my_data.receive_TW = receive_TW
        my_data.receive_CHN = receive_CHN
        my_data.analysis = analysis
        my_data.measure1 = option1
        my_data.measure2 = option2
        my_data.inventory = inventory
        my_data.round_profit = round_profit
        my_data.total_profit = total_profit
        db.session.commit()
        return render_template("round3_feedback.html", content = "testing",
        order_US=order_US, order_TW=order_TW, order_CHN=order_CHN, receive_US=receive_US, receive_TW=receive_TW, receive_CHN=receive_CHN, inventory=inventory, dem_cov=dem_cov, service_level=service_level, round_profit=format(round_profit, ",.2f"), total_profit=format(total_profit, ",.2f"), showCN = usedCN)
    else:
        query_profit = db.session.query(Data.total_profit).filter_by(id = 2).first()._asdict()
        query_inventory = db.session.query(Data.inventory).filter_by(id = 2).first()._asdict()
        profit_r2 = query_profit.get("total_profit")
        inventory_r2 = query_inventory.get("inventory")
        
        return render_template("round3.html", content = "testing", 
        profit_r2 = profit_r2, inventory_r2 = inventory_r2)

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


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True, port=33507)