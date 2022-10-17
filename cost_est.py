class CostEstimation:
    def __init__(self, parts, build):
        self.parts = parts
        self.build = build
        self.F = 0.06  #statistically found value
        self.machine_rate = 52546
        self.cost_gas = 60000
        self.cost_rl = 90000
        self.filter_porous = 127000 
        self.cost_mp = 50000

    def calculate_cost_material(self, part):
        material_type = {
            "inconel": 157300 * 8e-6,  # WON/kg*kg/mm3,
            "maraging_steel": 206800 * 8.0e-6,
            "ss316l": 205000 * 8.0e-6,
            "ti_grade2": 601700 * 4.51e-6,
            "ti64": 748000 * 4.43e-6 #it was 460000 but from KNU_Ti64 I noticed that material cost/kg is 748k
        }
        mat_cost = material_type.__getitem__(self.build['material_type'])

        cost_part = mat_cost * float(part['number_of_parts']) * float(part['part_volume'])
        cost_sup = mat_cost * float(part['number_of_parts']) * float(part['support_volume'])
        cost_scrap = cost_part * 0.15
        cost_mat = cost_part + cost_sup + cost_scrap

        return cost_mat

    def calculate_cost_build(self):
        if float(self.build['build_time']) >= 240:
            cost_filter = 2 * float(self.filter_porous)
        elif float(self.build['build_time']) < 240:
            cost_filter = float(self.filter_porous)
        cost_machine = float(self.build['build_time']) * float(self.machine_rate)
        cost_build = cost_machine + cost_filter + self.cost_gas + self.cost_rl
        return cost_build

    def calculate_cost_post(self):
        if self.build['wire_cut'] == 'True':
            cost_wc = 200000
        else:
            cost_wc = 0

        if self.build['heat_treat'] == 'True':
            cost_ht = 100000
        else:
            cost_ht = 0
        cost_post = self.cost_mp + cost_wc + cost_ht
        return cost_post

    def get_costs(self):
        cost_parts = []
        final_cost_parts = []
        parts_volume = 0

        for part in self.parts:
            cost_mat = float(self.calculate_cost_material(part))
            parts_volume += int(part['number_of_parts']) * (int(part['part_volume']) + int(part['support_volume']))
            cost_parts.append(cost_mat)

        cost_build = float(self.calculate_cost_build())
        cost_post = float(self.calculate_cost_post())

        total_cost = (cost_build + cost_post + sum(cost_parts)) / (1 - self.F)

        for part in self.parts:
            cost_part = ((int(part['number_of_parts']) * (int(part['part_volume']) + int(part['support_volume']))) / parts_volume) * total_cost
            final_cost_parts.append(cost_part)
        
        return final_cost_parts, total_cost

