# Labyrinth Seal

### Engine Notes
```python
in_to_m = 0.0254
c = .005 # nominal lab seal deflection
kp = c*23.33
fw = c*1.1
fh = c*10.73
sd = c*.8
sh = c*4.5
r_pt_inlet = 1.76
r_tooth_1 = r_pt_inlet+.03
r_tooth_2 = r_tooth_1+kp
r_tooth_3 = r_tooth_2+kp
r_seal_avg = (r_tooth_1+r_tooth_2+r_tooth_3)/3
seal_area = 2*math.pi*c*r_seal_avg
seal_area_m2 = seal_area*in_to_m**2
print('seal_area in^2:', seal_area)
print('seal_area m^2:', seal_area_m2)

# massflow characteristics
mdot_core = .35 # kg/s
k = 1.4 # air
r = 287.05  # air
t_o = 200 + 273 # post impeller temp in kelvin

p_inlet = 386821    # p inlet pascals
p_outlet = 101325*3 # 3 atmospheres
p_r = p_inlet/p_outlet

# mdot calculation
mdot_ideal = (p_inlet*seal_area_m2/t_o**.5) * ( 2*k/(r*(k-1))* ( (1/p_r)**(2/k) - (1/p_r)**((k+1)/k)))**.5
print('mdot ideal:', mdot_ideal)

cd = .405   # discharge coefficient
mdot_lab = cd*mdot_ideal
leakage_percent = 100*mdot_lab/mdot_core
print('leakage % :', leakage_percent)

# seal gap to area
def gap_to_area(gap):
    r_pt_inlet = 1.76
    r_tooth_1 = r_pt_inlet+.03
    r_tooth_2 = r_tooth_1+kp
    r_tooth_3 = r_tooth_2+kp
    r_seal_avg = (r_tooth_1+r_tooth_2+r_tooth_3)/3
    seal_area = 2*math.pi*gap*r_seal_avg
    seal_area_m2 = seal_area*in_to_m**2
    return seal_area_m2
gap_to_area(.005)
# massflows
def leakage_calc(seal_area_m2, mdot_core, t_o, p_inlet, p_outlet):
    p_r = p_inlet/p_outlet
    # mdot calculation
    mdot_ideal = (p_inlet*seal_area_m2/t_o**.5) * ( 2*k/(r*(k-1))* ( (1/p_r)**(2/k) - (1/p_r)**((k+1)/k)))**.5
    mdot_lab = cd*mdot_ideal
    leakage_percent = 100*mdot_lab/mdot_core
    return leakage_percent
leakage_calc(gap_to_area(.005), mdot_core, t_o, p_inlet, p_outlet)
```

### Equation
```python
# Lab Seal Pressures
ls_upstream = ['P_NI_Lab_Seal_Upstream_1', 'P_NI_Lab_Seal_Upstream_2', 'P_NI_Lab_Seal_Upstream_3', 'P_NI_Lab_Seal_Upstream_4']
df['Lab_Seal_Upstream_AVG'] = df[ls_upstream].mean(axis=1)
ls_downstream = ['P_NI_Lab_Seal_Downstream_1', 'P_NI_Lab_Seal_Downstream_2', 'P_NI_Lab_Seal_Downstream_3', 'P_NI_Lab_Seal_Downstream_4']
df['Lab_Seal_Downstream_AVG'] = df[ls_downstream].mean(axis=1)
fig_creator(df, 'elapsed_sec', ls_upstream, 'Elapsed Seconds', 'kPa', 'P_Lab_Seal_Up')
fig_creator(df, 'elapsed_sec', ls_downstream, 'Elapsed Seconds', 'kPa', 'P_Lab_Seal_Down')
fig_creator(df, 'elapsed_sec', ls_upstream+ls_downstream, 'Elapsed Seconds', 'kPa', 'P_Lab_Seal')

# lab seal delta at power
df['ls_delta'] = df['Lab_Seal_Upstream_AVG'] - df['Lab_Seal_Downstream_AVG']
```
