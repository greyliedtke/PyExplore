# Turbine Inlet Temperature


### T07
["T_NI_PT_Outlet_Duct_3", "T_NI_PT_Outlet_Duct_4", "T_NI_PT_Outlet_Duct_6", "T_NI_PT_Outlet_Duct_7"]

### Equation
```python

fuel_lhv = 43 * 1000  # kj/kg
air_cp = 1.101  # kJ/kgK ---   Average from estimated inlet and outlet temps

def turbine_inlet_temp_est(df, temp_cols, mdot_fuel, mdot_air, air_inlet):
    """
    mdot_fuel: kg/s of fuel
    air_inlet: PT Outlet average
    """
    heat_input_kw = fuel_lhv * mdot_fuel
    air_inlet = air_inlet + 273.15  # kelvin duct inlet to turbine
    dt = heat_input_kw / ((mdot_air + mdot_fuel) * air_cp)
    t_turbine_inlet = air_inlet + dt
    return t_turbine_inlet
```
