# Massflow

- Task07 engine: .38 kg/s
- 5k - .06 kg/s
- 
### Bellmouth Hardware
- [5 inch BM](https://airflownozzles.hy-grademetal.com/item/industrial/asme-air-flow-nozzles/afn-5)
- [Hose](https://www.mcmaster.com/5136K27/)
- [6x6 mesh](https://www.mcmaster.com/9227T55/)
- [30x30 mesh](https://www.mcmaster.com/9227T63/)
  

### Engine Notes
imp_area = 0.00314411  # m^2
imp_area_factor = 0.9  # impeller af
bm_area = 3.14159 * (5 * 0.0254) ** 2 / 4  # m^2
bm_area_factor = 0.90  # bm af

### Venturi Measurement
d_venturi_inlet = 2.067 # inches
d_venturi_throat = 1.2  # inches
c_d = 0.985  # cause re at throat is 4e5???p
beta = d_venturi_throat / d_venturi_inlet
bm_area = circle_area(2*in_to_m)   # m^2
bm_area_factor = .95       # bm af

### Equation
```python
def mass_flow_calc(amb_p, amb_t, inlet_pressure, inlet_temp, area, cd):
    # df['imp_mf'] = [mass_flow_calc(amb_p, amb_t, -inlet_p, inlet_temp=amb_t, area=imp_area, cd=imp_area_factor) for inlet_p in imp_pressure_avg_pa]
    # df['bm_mf'] = [mass_flow_calc(amb_p, amb_t, -inlet_p, inlet_temp=amb_t, area=bm_area, cd=bm_area_factor) for inlet_p in bm_avg_pa]
    # all variables in si units. https://www.grc.nasa.gov/www/k-12/rocket/mflchk.html. rearrange and include cd...
    p_ratio = (inlet_pressure + amb_p)/amb_p
    m_local = (2 * (p_ratio ** (-.4/1.4) - 1)/.4) ** .5
    mass_flow = (cd * area * amb_p / (amb_t ** .5)) * ((1.4 / inlet_temp) ** .5) * m_local * \
                ((1 + (.2 * (m_local ** 2))) ** (-.5 * 2.4 / .4))
    return mass_flow

def isentropic_flow(p_1, p_2, beta, c_d, a_2, dp=False):
    # isentropic flowrate for venturi
    if not dp:
        dp = p_1 - p_2
    try:
        tau = (dp + amb_p) / amb_p
        eta = (
            (k_air * tau ** (2 / k_air) / (k_air - 1))
            * ((1 - beta**4) / (1 - beta**4 * tau ** (2 / k_air)))
            * ((1 - tau ** ((k_air - 1) / k_air)) / (1 - tau))
        ) ** 0.5
        q_m = (c_d / ((1 - beta**4) ** 0.5)) * eta * a_2 * (2 * dp * rho_air) ** 0.5
    except:
        q_m = 0
    q_m = q_m.real
    return q_m

bm_mf = [mass_flow_calc(amb_p, amb_t, -inlet_p*1000, inlet_temp=amb_t, area=bm_area, cd=bm_area_factor) for inlet_p in df['P_Bellmouth']]
df['MF_BM'] = bm_mf
mf_venturi = [isentropic_flow(0, 0, beta, c_d, v_a_2, dp=dp*1000) for dp in df['P_Venturi']]
df['MF_V'] = mf_venturi
```
