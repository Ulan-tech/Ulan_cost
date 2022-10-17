from flask import Flask, render_template, request, jsonify
from cost_est import CostEstimation
from service import DataInjection
from models import Schema
from datetime import datetime
import uuid

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cost', methods =["GET", "POST"])
def cost():
    if request.method == "POST":
        data = request.get_json()

        parts = data['parts']
        build = data['build']

        build_id = int(datetime.now().timestamp()*1000)
        print(parts, "PARTS")
        print(build, "BUILD\n", build_id)
        cost_est = CostEstimation(parts, build)
 
        final_parts_cost, total_cost = cost_est.get_costs()

        data_injection = DataInjection(build_id) 

        for idx, part in enumerate(parts):
            data_injection.insert_part_details({
                                        'part_name': part['part_name'],
                                        'material_type': build['material_type'],
                                        'number_of_parts': part['number_of_parts'],
                                        'part_volume': part['part_volume'],
                                        'support_volume': part['support_volume'],
                                        'surface_area': part['surface_area'] or ':null',
                                        'box_volume': part['box_volume'] or ':null',
                                        'part_cost': final_parts_cost[idx],
                                        'build_id': build_id})
        data_injection.insert_build_details({
                                        'customer': build['customer'], 
                                        'material_type': build['material_type'],
                                        'hatch_distance': build['hatch_distance'] or ':null',
                                        'num_of_layers': build['num_of_layers'] or ':null',
                                        'layer_thickness': build['layer_thickness'] or ':null',
                                        'build_time': build['build_time'],
                                        'max_build_height': build['max_build_height'] or ':null',
                                        'scan_speed': build['scan_speed'] or ':null',
                                        'wire_cut': build['wire_cut'],
                                        'heat_treat': build['heat_treat'],
                                        'build_cost': total_cost,
                                        'total_cost': total_cost,
                                        'build_id': build_id})
        parts_cost = data_injection.read()
        print(parts_cost)        
        return jsonify(parts=parts_cost)


@app.route('/about')
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    Schema()
    app.run()
