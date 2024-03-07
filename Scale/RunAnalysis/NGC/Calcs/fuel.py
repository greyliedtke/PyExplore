
def fuel_flow(df):
    rho_fuel = .817 # kg/m^3
    hhv = 43E3 # MJ/kg
    df['fuel_kgs'] = df['VF_PLC_Fuel'] * rho_fuel / 60
    df['fuel_gph'] = df['VF_PLC_Fuel'] * 60 / 3.78541 
    df['fuel_energy'] = df['fuel_kgs'] * hhv
    df["fuel_eff"] = 100 * (df["kw_4wi"] / df['fuel_energy'])
    return df


