import sqlite3

class PartsAndBuilds:
    def __init__(self):
        self.conn = sqlite3.connect('slm.db')
        self.cur = self.conn.cursor()

    def read(self, build_id):
        res = self.cur.execute(f'select * from parts where build_id = {build_id}')
        parts = res.fetchall()
        return parts

    def insertPart(self, material_type, number_of_parts, part_volume, support_volume, scan_speed, surface_area, box_volume, build_id):
        part_query = f"""insert into parts """\
                f"""(
                        material_type,
                        number_of_parts,
                        part_volume,
                        support_volume,
                        scan_speed, 
                        surface_area,
                        box_volume,
                        build_id
                    )""" \
                f"""values ('{material_type}',
                            {number_of_parts},
                            {part_volume},
                            {support_volume}, 
                            {scan_speed},
                            {surface_area}, 
                            {box_volume}, 
                            {build_id}
                    )"""
        print(part_query)
        return self.cur.execute(part_query)
         
    def insertBuild(self, build_id, customer, material_type, hatch_distance, num_of_layers, layer_thickness, build_time, max_build_height, wire_cut, heat_treat):
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
                        wire_cut,
                        heat_treat
                    )""" \
                f"""values ({build_id},
                            '{customer}',
                            '{material_type}',
                            {hatch_distance},
                            {num_of_layers},
                            {layer_thickness},
                            {build_time},
                            {max_build_height},
                            {wire_cut},
                            {heat_treat}
                    )"""
        print(build_query)
        return self.cur.execute(build_query)
   
class DataInjection:
    def __init__(self, build_id):
        self.model = PartsAndBuilds()
        self.build_id = build_id
    
    def read(self):
        return self.model.read(self.build_id)
    
    def insert_part_details(self, params):
        return self.model.insertPart(
            params['material_type'], 
            params['number_of_parts'],
            params['part_volume'],
            params['support_volume'],
            params['scan_speed'], 
            params['surface_area'], 
            params['box_volume'],  
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
            params['wire_cut'], 
            params['heat_treat'])