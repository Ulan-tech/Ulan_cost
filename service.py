import sqlite3
import uuid

class DataInjection:
    def __init__(self):
        self.conn = sqlite3.connect('slm.db', timeout=10)

    def read(self):
        cur = self.conn.cursor()
        res = cur.execute('select * from part_information')
        print(res.fetchall())
        return 0

    def insert(self, customer, material_type, hatch_distance, num_of_layers, scan_speed, layer_thickness, build_time, number_of_parts,part_volume,support_volume,
               surface_area, box_volume, max_build_height, wire_cut, heat_treat, build_cost, mat_cost, build_id):
        
        part_id = 1
        cur = self.conn.cursor()
        part_query = f"""insert into "part_information" """\
                f"""(
                        customer,
                        part_id,
                        material_type,
                        number_of_parts,
                        part_volume,
                        support_volume,
                        scan_speed, 
                        surface_area,
                        box_volume,
                        material_cost,
                        build_id
                    )""" \
                f"""values ('{customer}',
                            {part_id},
                            '{material_type}',
                            {number_of_parts},
                            {part_volume},
                            {support_volume}, 
                            {scan_speed},
                            {surface_area}, 
                            {box_volume}, 
                            {mat_cost},
                            {build_id}
                    )"""
        print(part_query)
        build_query = f"""insert into "build_information" """\
                f"""(
                        build_id,
                        material_type,
                        hatch_distance,
                        num_of_layers,
                        layer_thickness,
                        build_time,
                        max_build_height,
                        wire_cut,
                        heat_treat,
                        build_cost
                    )""" \
                f"""values ({build_id},
                            '{material_type}',
                            {hatch_distance},
                            {num_of_layers},
                            {layer_thickness},
                            {build_time},
                            {max_build_height},
                            {wire_cut},
                            {heat_treat},
                            {build_cost}
                    )"""
        total_cost = build_cost + mat_cost
        part_cost = total_cost
        print(build_query)
        cost_query = f"""insert into "cost_information" """\
                f"""(
                        part_id,
                        part_cost,
                        total_cost   
                    )""" \
                f"""values (
                        {part_id},
                        {part_cost},
                        {total_cost} 
                    )"""
        print(cost_query)
        cur.execute(part_query)
        # self.conn.commit()
        # self.conn.close()
        # cur = self.conn.cursor()
        cur.execute(build_query)
        # cur.commit()
        # cur.close()
        # cur = self.conn.cursor()

        cur.execute(cost_query)
        self.conn.commit()
        cur.close()

        return total_cost, part_cost
    
class CostEstimationService:
    def __init__(self):
        self.model = DataInjection()
    
    def read(self):
        return self.model.read()
        
    def create(self, params):
        return self.model.insert(params['customer'], 
        params['material_type'], 
        params['hatch_distance'], 
        params['num_of_layers'], 
        params['scan_speed'], 
        params['layer_thickness'], 
        params['build_time'], 
        params['number_of_parts'],
        params['part_volume'],
        params['support_volume'],
        params['surface_area'], 
        params['box_volume'], 
        params['max_build_height'], 
        params['wire_cut'], 
        params['heat_treat'], 
        params['build_cost'], 
        params['mat_cost'], 
        params['build_id'])