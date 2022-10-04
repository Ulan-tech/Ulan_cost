# 1.import sqlite
import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('slm.db')
        self.create_part_information_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_part_information_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "part_information" (
            customer text,
            material_type text,
            hatch_distance NUMERIC,
            num_of_layers NUMERIC,
            scan_speed NUMERIC, 
            layer_thickness NUMERIC,
            build_time NUMERIC,
            number_of_parts NUMERIC,
            part_volume NUMERIC,
            support_volume NUMERIC,
            surface_area NUMERIC,
            box_volume NUMERIC,
            max_build_height NUMERIC,
            wire_cut text,
            heat_treat text,
            total_cost NUMERIC
            
        );
        """
        self.conn.execute(query)