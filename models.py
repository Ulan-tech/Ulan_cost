# 1.import sqlite
import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('slm.db')
        self.create_part_information_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_part_information_table(self):
        part_query = """
        CREATE TABLE IF NOT EXISTS "part_information" (
            customer text,
            part_id INTEGER,
            material_type text,
            number_of_parts NUMERIC,
            part_volume NUMERIC,
            support_volume NUMERIC,
            scan_speed NUMERIC, 
            surface_area NUMERIC,
            box_volume NUMERIC,
            material_cost NUMERIC,
            build_id INTEGER
        );
        """

        build_query = """
        CREATE TABLE IF NOT EXISTS "build_information" (
            build_id INTEGER,
            material_type text,
            hatch_distance NUMERIC,
            num_of_layers NUMERIC,
            layer_thickness NUMERIC,
            build_time NUMERIC,
            max_build_height NUMERIC,
            wire_cut text,
            heat_treat text,
            build_cost NUMERIC
        );
        """

        cost_query = """
        CREATE TABLE IF NOT EXISTS "cost_information" (
            part_id INTEGER,
            part_cost NUMERIC,
            total_cost NUMERIC      
        );
        """

        self.conn.execute(part_query)
        self.conn.execute(build_query)
        self.conn.execute(cost_query)