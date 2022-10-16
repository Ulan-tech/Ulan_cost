# 1.import sqlite
import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('slm.db')
        self.drop_tables()
        self.create_tables()
        # Why are we calling user table before to_do table
        # what happens if we swap them?
    def drop_tables(self):
        q1 = "DROP table parts"
        q2 = "DROP table builds"
        self.conn.execute(q1)
        self.conn.execute(q2)

    def create_tables(self):
        part_query = """
        CREATE TABLE IF NOT EXISTS "parts" (
            part_id INTEGER PRIMARY KEY AUTOINCREMENT,
            part_name TEXT,
            material_type TEXT,
            number_of_parts NUMERIC,
            part_volume NUMERIC,
            support_volume NUMERIC,
            surface_area NUMERIC,
            box_volume NUMERIC,
            part_cost NUMERIC,
            build_id INTEGER
        );
        """

        build_query = """
        CREATE TABLE IF NOT EXISTS "builds" (
            build_id INTEGER PRIMARY KEY,
            customer TEXT,
            material_type TEXT,
            hatch_distance NUMERIC,
            num_of_layers NUMERIC,
            layer_thickness NUMERIC,
            build_time NUMERIC,
            max_build_height NUMERIC,
            scan_speed NUMERIC, 
            wire_cut TEXT,
            heat_treat TEXT,
            build_cost NUMERIC,
            total_cost NUMERIC
        );
        """
        self.conn.execute(part_query)
        self.conn.execute(build_query)
        # self.conn.execute(cost_query)