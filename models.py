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
            layer_thickness NUMERIC,
            part_volume NUMERIC,
            support_volume NUMERIC,
            part_surface_area NUMERIC,
            number_parts NUMERIC,
            material text,
            final_cost NUMERIC
        );
        """
        self.conn.execute(query)