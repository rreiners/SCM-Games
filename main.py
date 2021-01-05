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
    id = db.Column(db.Integer, primary_key=True)
    quantity_1 = db.Column(db.Integer)
    quantity_2 = db.Column(db.Integer)

    def __init__(self, quantity_1, quantity_2):
        self.quantity_1 = quantity_1
        self.quantity_2 = quantity_2


@app.route('/', methods=['GET','POST'])
def home():

    if request.method == 'POST':
        return redirect('/round1')
    else:
        return render_template("home.html", content = "testing")

@app.route('/round1/', methods=['GET', 'POST'])
def round1():

    if request.method == 'POST':
        order_1 = int(request.form['order_quantity_1'])
        order_2 = int(request.form['order_quantity_2'])
        result = order_1 + order_2

        if request.form['Button'] == 'Modal':
            flash(result)
            return redirect(url_for('round1'))
        else:
            my_data = Data(order_1, order_2)
            db.session.add(my_data)
            db.session.commit()
            return render_template("round1_feedback.html", 
            order_1 = order_1, order_2 = order_2, value=result, content = "testing")
    else:
        return render_template("round1.html", content = "testing")



@app.route('/round1/feedback/', methods=['GET', 'POST'])
def round1_feedback():

    if request.method == 'POST':
        return render_template("round1_feedback.html", content = "testing")
    else:
        return render_template("round1_feedback.html", content = "testing")


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