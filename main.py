import os 
from flask import Flask, request, render_template, render_template_string, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

template_dir = os.path.abspath('/Users/robinreiners/Documents/GitHub/SCM-Games/templates')

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

@app.route('/round1', methods=['GET', 'POST'])
def round1():

    if request.method == 'POST':
        order_1 = int(request.form['order_quantity_1'])
        order_2 = int(request.form['order_quantity_2'])
        result = order_1 + order_2

        if request.form['Button'] == 'Modal':
            return render_template("round1.html", show_modal= 1, 
            value=result, content = "testing")
        else:
            my_data = Data(order_1, order_2)
            db.session.add(my_data)
            db.session.commit()
    else:
        return render_template("round1.html", content = "testing")

    return render_template("round1.html", content = "testing")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
