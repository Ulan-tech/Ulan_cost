class CostEstimation:
    def __init__(self, build_time, m_type, number_of_parts, part_volume, support_volume, wire_cut, heat_treat):
        self.build_time = build_time
        self.m_type = m_type
        self.number_of_parts = number_of_parts
        self.part_volume = part_volume
        self.support_volume = support_volume
        self.wire_cut = wire_cut
        self.heat_treat = heat_treat
        self.F = 0.06  #statistically found value
        self.machine_rate = 52546
        self.cost_gas = 60000
        self.cost_rl = 90000
        self.filter_porous = 127000 
        self.cost_mp = 50000

    def calculate_cost_material(self):
        material_type = {
            "inconel": 157300 * 8e-6,  # WON/kg*kg/mm3,
            "maraging_steel": 206800 * 8.0e-6,
            "ss316l": 205000 * 8.0e-6,
            "ti_grade2": 601700 * 4.51e-6,
            "ti64": 748000 * 4.43e-6 #it was 460000 but from KNU_Ti64 I noticed that material cost/kg is 748k
        }
        mat_cost = material_type.__getitem__(self.m_type)

        cost_part = mat_cost * float(self.number_of_parts) * float(self.part_volume)
        cost_sup = mat_cost * float(self.number_of_parts) * float(self.support_volume)
        cost_scrap = cost_part * 0.15
        cost_mat = cost_part + cost_sup + cost_scrap

        return cost_mat

    def calculate_cost_build(self):
        if float(self.build_time) >= 240:
            cost_filter = 2 * float(self.filter_porous)
        elif float(self.build_time) < 240:
            cost_filter = float(self.filter_porous)
        cost_machine = float(self.build_time) * float(self.machine_rate)
        cost_build = cost_machine + cost_filter + self.cost_gas + self.cost_rl
        return cost_build

    def calculate_cost_post(self):
        if self.wire_cut == 'on':
            cost_wc = 200000
        else:
            cost_wc = 0

        if self.heat_treat == 'on':
            cost_ht = 100000
        else:
            cost_ht = 0
        cost_post = self.cost_mp + cost_wc + cost_ht
        return cost_post

    def calculate_cost_build_total(self):
        cost_mat = float(self.calculate_cost_material())
        cost_build = float(self.calculate_cost_build())
        cost_post = float(self.calculate_cost_post())
        cost_build_total = (cost_build + cost_post) / (1 - self.F)
        cost_part_total = cost_mat/(1 - self.F)
        return cost_build_total, cost_part_total
    # # cost per part
    # cost_per_part = cost_total/number_of_parts
