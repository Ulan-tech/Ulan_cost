from functools import total_ordering
import sqlite3

class PartsAndBuilds:
    def __init__(self):
        self.conn = sqlite3.connect('slm.db')
        self.cur = self.conn.cursor()
    
    def read(self, build_id):
        # res = self.cur.execute(f"""
        #     SELECT 
        #         *
        #     FROM parts
        #     """)
        res = self.cur.execute(f"""
            SELECT 
                p.part_name,
                p.part_cost, 
                b.total_cost,
                p.number_of_parts
            FROM 
                parts as p 
            JOIN 
                builds as b 
            ON 
                p.build_id = b.build_id 
            WHERE 
                b.build_id = {build_id}
            """)
        parts = res.fetchall()
        return parts

    def insertPart(self, part_name, material_type, number_of_parts, part_volume, support_volume, surface_area, box_volume, part_cost, build_id):
        part_query = f"""insert into parts """\
                f"""(
                        part_name,
                        material_type,
                        number_of_parts,
                        part_volume,
                        support_volume,
                        surface_area,
                        box_volume,
                        part_cost,
                        build_id
                    )""" \
                f""" values('{part_name}',
                            '{material_type}',
                            {number_of_parts},
                            {part_volume},
                            {support_volume}, 
                            {surface_area}, 
                            {box_volume}, 
                            {part_cost},
                            {build_id}
                    )"""
        print(part_query)
        return self.cur.execute(part_query, {'null':None})
         
    def insertBuild(self, build_id, customer, material_type, hatch_distance, num_of_layers, layer_thickness, build_time, max_build_height, scan_speed, wire_cut, heat_treat, build_cost, total_cost):
        build_query = f"""insert into builds """\
                f"""(
                        build_id,
                        customer,
                        material_type,
                        hatch_distance,
                        num_of_layers,
                        layer_thickness,
                        build_time,
                        max_build_height,
                        scan_speed, 
                        wire_cut,
                        heat_treat,
                        build_cost,
                        total_cost
                    )""" \
                f""" values({build_id},
                            '{customer}',
                            '{material_type}',
                            {hatch_distance},
                            {num_of_layers},
                            {layer_thickness},
                            {build_time},
                            {max_build_height},
                            {scan_speed},
                            {wire_cut},
                            {heat_treat},
                            {build_cost},
                            {total_cost}
                    )"""
        print(build_query)
        return self.cur.execute(build_query, {'null':None})
   
class DataInjection:
    def __init__(self, build_id):
        self.model = PartsAndBuilds()
        self.build_id = build_id
    
    def read(self):
        return self.model.read(self.build_id)
    
    def insert_part_details(self, params):
        return self.model.insertPart(
            params['part_name'], 
            params['material_type'], 
            params['number_of_parts'],
            params['part_volume'],
            params['support_volume'],
            params['surface_area'], 
            params['box_volume'],  
            params['part_cost'],  
            params['build_id'])
    
    def insert_build_details(self, params):
        return self.model.insertBuild(
            params['build_id'],
            params['customer'], 
            params['material_type'], 
            params['hatch_distance'], 
            params['num_of_layers'], 
            params['layer_thickness'], 
            params['build_time'], 
            params['max_build_height'], 
            params['scan_speed'], 
            params['wire_cut'], 
            params['heat_treat'],
            params['build_cost'],
            params['total_cost'])