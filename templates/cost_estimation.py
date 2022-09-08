inconel = 'inconel_slm'
maraging_steel = 'maraging_steel_slm'
ss316l = 'sus316l'
ti_grade2 = 'cp_ti'
ti64 = 'ti6al4V'
mat_cost_kg = 0

# %% Cost of build parameters all in KRW
F = 0.06  #statistically found value
c_machrate = 52546
c_gas = 60000
c_rl = 90000
c_filter_porous = 127000 #it was 400000

# %% Post-processing cost
c_mp = 50000
# c_wc = 200000  # let it stay as constant for now
# c_ht = 100000  # this is an assumed value, it should be different for various materials

# %%Input entries
number_of_parts = int(input("Number of a part-1: "))   #"Number of Parts"
t_build = int(input("Total build time from the SLM machine: ")) #"Overall build time"

material_type = {
    "inconel": 157300 * 8e-6,  # WON/kg*kg/mm3,
    "maraging_steel": 206800 * 8.0e-6,
    "ss316l": 205000 * 8.0e-6,
    "ti_grade2": 601700 * 4.51e-6,
    "ti64": 748000 * 4.43e-6, #it was 460000 but from KNU_Ti64 I noticed that material cost/kg is 748k
}
#Material type

#%% Input material type and number of different parts:
m_type, different_parts = 'ti64', 2
mat_cost = material_type.__getitem__(m_type)
c_machine = t_build * c_machrate

#%% According to different_parts:
part_sup_vol = []
print(type(part_sup_vol))

if different_parts > 1:  # corresponds to number of different parts
    for i in range(1, different_parts + 1):
        volume = input(
            "Enter corresponding number of parts + part volume + support volume for part #{0}".format(i)).split('+')
        part_sup_vol.append([int(volume[0]), float(volume[1]), float(volume[2])])

    cost_part = 0
    cost_sup = 0
    for j in range(len(part_sup_vol)):
        cost_part = cost_part + mat_cost * part_sup_vol[j][0] * part_sup_vol[j][1]
        cost_sup = cost_sup + mat_cost * part_sup_vol[j][0] * part_sup_vol[j][2]
    cost_scrap = cost_part * 0.15
else:
    volume = input("Enter corresponding number of parts + part volume + support volume for part #{0}".format(1)).split(
        '+')
    cost_part = mat_cost * int(volume[0]) * float(volume[1])
    cost_sup = mat_cost * int(volume[0]) * float(volume[2])
    cost_scrap = cost_part * 0.15

print(cost_part)
print(cost_sup)

#%% Filter change is needed if t_build>=240
if t_build >= 240:
    c_filter = 2 * c_filter_porous
elif t_build < 240:
    c_filter = c_filter_porous


#%% Asking whether build job need wire cutting and heat treatment

cp_mat = cost_part + cost_sup + cost_scrap
c_build = c_machine + c_filter + c_gas + c_rl

wire_cut = input('Does the build job need wire cutting?')
heat_treat = input('Does the build job need heat treatment?')

if wire_cut == 'N':
    c_wc = 0
else:
    c_wc = 200000

if heat_treat == 'N':
    c_ht = 0
else:
    c_ht = 100000

c_post = c_mp + c_wc + c_ht

#%% total cost calculation
if different_parts == 1:
    c_total =  (cp_mat + c_build + c_post)*1 / (1 - F)
    print('Total cost is', c_total)
    cost_per_part = c_total/int(volume[0])
    print('Cost per part is', cost_per_part)
else:
    c_total =  (cp_mat + c_build + c_post)*1 / (1 - F)
    print('Total cost is', c_total)
#%% c_temp
c_temp = 0
for i in range(len(part_sup_vol)):
    c_temp = c_temp + (part_sup_vol[i][0] * (part_sup_vol[i][1] + part_sup_vol[i][2]))
print(c_temp)

#%%cost ratio
cost_ratio_total = c_total/c_temp
print(cost_ratio_total)

#%% finding cost per part
c_i = []
for i in range(len(part_sup_vol)):
    c_i.append(part_sup_vol[i][0] * (part_sup_vol[i][1] + part_sup_vol[i][2]) * cost_ratio_total)
print(c_i)

