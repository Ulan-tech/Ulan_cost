class PartsAndBuilds:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()
    
    def read(self, build_id):
        self.cursor.execute(f"""
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

        self.conn.commit()

        parts = self.cursor.fetchall()

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
                f""" values(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )"""
        query = self.cursor.mogrify(part_query, (part_name,
                                        material_type,
                                        number_of_parts,
                                        part_volume,
                                        support_volume, 
                                        surface_area, 
                                        box_volume, 
                                        part_cost,
                                        build_id)
                            )
        print(query)
        self.cursor.execute(query)

        self.conn.commit()

        return

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
                f""" values(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s, 
                        %s,
                        %s,
                        %s,
                        %s
                    )"""
        print(build_query)
        query = self.cursor.mogrify(build_query, (
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
                                total_cost)
                            )
        print(query)
        self.cursor.execute(query)

        self.conn.commit()

        return
   
class DataInjection:
    def __init__(self, conn, build_id):
        self.model = PartsAndBuilds(conn)
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