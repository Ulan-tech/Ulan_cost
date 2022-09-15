from flask import Flask, render_template, request
from cost_est import CostEstimation
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
        material_type = request.form.get("material_type")
        number_of_parts = request.form.get("num_of_parts")
        part_volume = request.form.get("part_volume")
        support_volume = request.form.get("support_volume")
        wire_cut = request.form.get("wire_cut")
        heat_treat = request.form.get("heat_treat")
        build_time = request.form.get("build_time")
        print("Customer name is ", customer)
        print("type is ", material_type)
        print("type is ", number_of_parts)
        print("type is ", part_volume)
        print("type is ", support_volume)
        print("type is ", wire_cut)
        print("type is ", heat_treat)
        cost_est = CostEstimation(build_time, material_type, number_of_parts, part_volume, support_volume, wire_cut, heat_treat)
        t = cost_est.calculate_cost_total()
        # CostEstimationService().create({'customer': customer, })
        # print("Total cost is ", total_cost)

    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    Schema()
    app.run()
