from flask import Flask, render_template, request
from service import CostEstimationService
app = Flask(__name__)
app.debug = True

@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/cost', methods =["GET", "POST"])
def cost():
    if request.method == "POST":
       # getting input with name = fname in HTML form
        customer = request.form.get("customer")
        layer_thicknes = request.form.get("customer")
        CostEstimationService().create({'customer': customer, })

    return render_template("home.html")

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html', title='about')

if __name__ == '__main__':
    Schema()
    app.run()
