from flask import Flask, render_template, request, jsonify
from cost_est import CostEstimation
from service import DataInjection
from models import Schema
from datetime import datetime
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
        
conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)

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

        data_injection = DataInjection(conn, build_id) 

        for idx, part in enumerate(parts):
            data_injection.insert_part_details({
                                        'part_name': part['part_name'],
                                        'material_type': build['material_type'],
                                        'number_of_parts': int(part['number_of_parts']) if part['number_of_parts'] else None,
                                        'part_volume': float(part['part_volume']) if part['part_volume'] else None,
                                        'support_volume': float(part['support_volume']) if part['support_volume'] else None,
                                        'surface_area': float(part['surface_area']) if part['surface_area'] else None,
                                        'box_volume': float(part['box_volume']) if part['box_volume'] else None,
                                        'part_cost': float(final_parts_cost[idx]) if final_parts_cost[idx] else None,
                                        'build_id': build_id})
        data_injection.insert_build_details({
                                        'customer': build['customer'], 
                                        'material_type': build['material_type'],
                                        'hatch_distance': float(build['hatch_distance']) if build['hatch_distance'] else None,
                                        'num_of_layers': int(build['num_of_layers']) if build['num_of_layers'] else None,
                                        'layer_thickness': float(build['layer_thickness']) if build['layer_thickness'] else  None,
                                        'build_time': float(build['build_time']) if build['build_time'] else None,
                                        'max_build_height': float(build['max_build_height']) if build['max_build_height'] else None,
                                        'scan_speed': float(build['scan_speed']) if build['scan_speed'] else None,
                                        'wire_cut': build['wire_cut'],
                                        'heat_treat': build['heat_treat'],
                                        'build_cost': float(total_cost) if total_cost else None,
                                        'total_cost': float(total_cost) if total_cost else None,
                                        'build_id': int(build_id) if build_id else None})
        parts_cost = data_injection.read()
        print(parts_cost)        
        return jsonify(parts=parts_cost)


@app.route('/about')
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    Schema(conn)
    app.run()
