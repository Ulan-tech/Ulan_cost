
class Schema:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        # self.drop_tables()
        self.create_tables()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def drop_tables(self):
        q1 = "DROP table parts"
        q2 = "DROP table builds"
        
        self.cursor.execute(q1)
        self.cursor.execute(q2)
        
        self.conn.commit()

        return self.conn.close()


    def create_tables(self):
        part_query = """
        CREATE TABLE IF NOT EXISTS parts (
            part_id SERIAL PRIMARY KEY,
            part_name TEXT,
            material_type TEXT,
            number_of_parts INTEGER,
            part_volume DOUBLE PRECISION,
            support_volume DOUBLE PRECISION,
            surface_area DOUBLE PRECISION,
            box_volume DOUBLE PRECISION,
            part_cost DOUBLE PRECISION,
            build_id BIGINT
        );
        """

        build_query = """
        CREATE TABLE IF NOT EXISTS builds (
            build_id BIGINT PRIMARY KEY,
            customer TEXT,
            material_type TEXT,
            hatch_distance DOUBLE PRECISION,
            num_of_layers INTEGER,
            layer_thickness DOUBLE PRECISION,
            build_time DOUBLE PRECISION,
            max_build_height DOUBLE PRECISION,
            scan_speed DOUBLE PRECISION, 
            wire_cut TEXT,
            heat_treat TEXT,
            build_cost DOUBLE PRECISION,
            total_cost DOUBLE PRECISION
        );
        """

        self.cursor.execute(part_query)
        self.cursor.execute(build_query)

        self.conn.commit()
