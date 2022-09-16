import sqlite3

class PartInfoModel:
    TABLENAME = "part_information"

    def __init__(self):
        self.conn = sqlite3.connect('slm.db')

    def insert(self, customer, material_type, hatch_distance, num_of_layers, scan_speed, layer_thickness, build_time, number_of_parts,part_volume,support_volume,
               surface_area, box_volume, max_build_height, wire_cut, heat_treat, total_cost):
        query = f"""insert into {self.TABLENAME} """\
                f"""(
                        customer,
                        material_type,
                        hatch_distance,
                        num_of_layers,
                        scan_speed, 
                        layer_thickness,
                        build_time,
                        number_of_parts,
                        part_volume,
                        support_volume,
                        surface_area,
                        box_volume,
                        max_build_height,
                        wire_cut,
                        heat_treat,
                        total_cost
                    ))""" \
                f"""values ('{customer}',
                            '{material_type}',
                            {hatch_distance},
                            {num_of_layers},
                            {scan_speed}
                            {layer_thickness},
                            {build_time},
                            {number_of_parts},
                            {part_volume},
                            {support_volume}, 
                            {surface_area}, 
                            {box_volume}, 
                            {max_build_height},
                            {wire_cut},
                            {heat_treat}, 
                            {total_cost}
                    )"""
        
        result = self.conn.execute(query)

        return result

class CostEstimationService:
    def __init__(self):
        self.model = PartInfoModel()
        
    def create(self, params):
        return self.model.create(params["customer"], params["Description"])