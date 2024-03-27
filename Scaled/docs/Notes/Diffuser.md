# Diffuser

### Engine Notes


### Equation
```python
# ------------------- Diffuser -----------------------------------------
def diffuser_calcs(df):
    df['diffuser_rho'] =101325/(( 273.15+df['T_PLC_Turbine_Exit_1'])*287.05)

    cba = 3.14158*(1.125*.0254)**2/4    # center body area
    diffuser_inlet_a = 3.14158*(3.265*.0254)**2/4 - cba
    diffuser_outlet_a = 3.14158*(6.064*.0254)**2/4 - cba

    df['dif_inlet_v'] = df['imp_mf']/(diffuser_inlet_a*df['diffuser_rho'])
    df['dif_outlet_v'] = df['imp_mf']/(diffuser_outlet_a*df['diffuser_rho'])

    df['dif_inlet_dp'] = .5*df['diffuser_rho']*df['dif_inlet_v']**2/1000
    df['dif_outlet_dp'] = .5*df['diffuser_rho']*df['dif_outlet_v']**2/1000
    return df


# Venturi flowrate
# v = df["MF_Venturi"] / (rho * a_diffuser)
# df["cp_diffuser"] = p_psdp / (0.5 * rho * v**2)
```
