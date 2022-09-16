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
        hatch_distance = request.form.get("hatch_distance")
        num_of_layers = request.form.get("num_of_layers")
        scan_speed = request.form.get("scan_speed")


        build_time = request.form.get("build_time")
        number_of_parts = request.form.get("num_of_parts")
        part_volume = request.form.get("part_volume")
        support_volume = request.form.get("support_volume")
        surface_area = request.form.get("surface_area")
        box_volume = request.form.get("box_volume")
        max_build_height = request.form.get("max_build_height")
        wire_cut = request.form.get("wire_cut")
        heat_treat = request.form.get("heat_treat")

        print("Customer name is ", customer)
        print("Material type is ", material_type)
        print("Hatch distance is ", hatch_distance)
        print("Number of layers is ", num_of_layers )
        print("Scan speed is ", scan_speed)

        print("Build time is ", build_time)

        print("Number of parts is ", number_of_parts)
        print("Part volume is ", part_volume)
        print("Support volume is ", support_volume)
        print("Surface area is ", surface_area)
        print("Bounding box volume is ", box_volume)
        print("Max build height is ", max_build_height)

        print("Use wire cut?:  ", wire_cut)
        print("Heat treatment?: ", heat_treat)

        cost_est = CostEstimation(build_time, material_type, number_of_parts, part_volume, support_volume, wire_cut, heat_treat)
        # t = cost_est.calculate_cost_total()
        # CostEstimationService().create({'customer': customer, })
        # print("Total cost is ", total_cost)

    return render_template("home.html")

# def calculate():
#     cost=''
#     if request.method=='POST' and 'customer' in request.form and 'material_type' in request.form:
#         Customer=request.form.get('customer')
#         Material_type=request.form.get('material_type')

    #
    #
    # return render_template("index.html", cost=cost)








questions = []
@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if request.form['name'] and request.form['ques']:
           questions.append({'name': request.form['name'], 'question': request.form['ques']})
    return render_template('def.html', questions=questions)







@app.route('/about')
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    Schema()
    app.run()
