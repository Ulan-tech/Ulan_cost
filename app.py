from flask import Flask, render_template, request
from service import CostEstimationService
from models import Schema

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cost', methods =["GET", "POST"])
def cost():
    if request.method == "POST":
       # getting input with name = fname in HTML form
        customer = request.form.get("customer")
        layer_thickness = request.form.get("customer")
        CostEstimationService().create({'customer': customer, })

    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    Schema()
    app.run()
