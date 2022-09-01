import sqlite3

class PartInfoModel:
    TABLENAME = "part_information"

    def __init__(self):
        self.conn = sqlite3.connect('slm.db')

    def create(self, customer, layer_thickness, part_volume, support_volume, part_surface_area, number_parts, material, final_cost):
        query = f"""insert into {self.TABLENAME} """\
                f"""(
                        customer, 
                        layer_thickness,
                        part_volume,
                        support_volume,
                        part_surface_area,
                        number_parts,
                        material,
                        final_cost
                    ))""" \
                f"""values ('{customer}',
                            {layer_thickness}, 
                            {part_volume}, 
                            {support_volume}, 
                            {part_surface_area}, 
                            {number_parts}, 
                            "{material}", 
                            {final_cost}
                    )"""
        
        result = self.conn.execute(query)

        return result

class CostEstimationService:
    def __init__(self):
        self.model = PartInfoModel()
        
    def create(self, params):
        return self.model.create(params["customer"], params["Description"])