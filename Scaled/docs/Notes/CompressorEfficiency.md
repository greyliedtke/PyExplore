# Compressor Efficiency

### Engine Notes
Effective Compressor Efficiency - low compressor efficiencies if power turbine speed too low

Sometimes performed on ducts or pt exit...
df['t_eff_PT_Exit'] = ((pr**(.4/1.4)-1)/(t_rc-1))*100
t_rc_duct = (df['PT_Duct_Avg_T']+273.15)/(df['T_Avg_Inlet']+273.15)
df['t_eff_PT_Duct'] = ((pr**(.4/1.4)-1)/(t_rc_duct-1))*100



### Equation
```python
# ------------------- Compressor Efficiency -----------------------------------------
# def compressor_eff(df):
#     # 
#     t_rc = (df["PT_exit_Avg_T"] + 273.15) / (df["T_Avg_Inlet"] + 273.15)
#     pr = df["PR"]
#     df["t_eff_PT_Exit"] = ((pr ** (0.4 / 1.4) - 1) / (t_rc - 1)) * 100

def compressor_eff(inlet_temp, outlet_temp, pressure_ratio, gamma):
    """
    Script to calculate compressor efficiency
    https://www.grc.nasa.gov/www/k-12/airplane/compth.html
    3 is power turbine temperature.
    rearrange for efficiency
    """
    inlet_temp_k = inlet_temp + 273.15
    outlet_temp_k = outlet_temp + 273.15
    t_rc = inlet_temp_k / (outlet_temp_k - inlet_temp_k)
    n = t_rc * (pressure_ratio ** ((gamma - 1) / gamma) - 1)

    # if n > 1 or n < 1:
    #     n = 0

    return n
```
