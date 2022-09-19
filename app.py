from flask import Flask, render_template, request
from cost_est import CostEstimation
from service import CostEstimationService
from models import Schema
import uuid

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
        layer_thickness = request.form.get("layer_thickness")

        build_time = request.form.get("build_time")
        number_of_parts = request.form.get("num_of_parts")
        part_volume = request.form.get("part_volume")
        support_volume = request.form.get("support_volume")
        surface_area = request.form.get("surface_area")
        box_volume = request.form.get("box_volume")
        max_build_height = request.form.get("max_build_height")
        wire_cut = request.form.get("wire_cut")
        heat_treat = request.form.get("heat_treat")

        if wire_cut == 'on':
            wire_cut = 1
        else:
            wire_cut = 0
        if heat_treat == 'on':
            heat_treat = 1
        else:
            heat_treat = 0

        build_id = 1

        print("Customer name is ", customer)
        print("Material type is ", material_type)
        print("Hatch distance is ", hatch_distance)
        print("Number of layers is ", num_of_layers )
        print("Scan speed is ", scan_speed)
        print("Layer thickness is ", layer_thickness)

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
        build_cost, material_cost = cost_est.calculate_cost_build_total()
        print("Build cost is ", build_cost)
        print("Material cost is ", material_cost)

        CostEstimationService().create({'customer': customer, 
                                        'material_type': material_type,
                                        'hatch_distance': hatch_distance,
                                        'num_of_layers': num_of_layers,
                                        'scan_speed': scan_speed,
                                        'layer_thickness': layer_thickness,
                                        'build_time': build_time,
                                        'number_of_parts': number_of_parts,
                                        'part_volume': part_volume,
                                        'support_volume': support_volume,
                                        'surface_area': surface_area,
                                        'box_volume': box_volume,
                                        'max_build_height': max_build_height,
                                        'wire_cut': wire_cut,
                                        'heat_treat': heat_treat,
                                        'build_cost': build_cost,
                                        'mat_cost': material_cost,
                                        'build_id': build_id,
                                        })
        print('Saved')
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    Schema()
    app.run()
