# SoCalGas Calculations

- Mostly from seamus


### Equation
```python
def methane_calcs(df, prefix):
    # methane calculation function to perform calculations and append to df with prefix on column
    vent_d = .003535
    # vent_d = .0025
    venturi = {
        "A": (math.pi / 4) * vent_d ** 2,
        "CD": .985  # discharge coefficient
    }
    methane = {
        "gamma": 1.32,  # Ratio of specific heats
        "Cp": 2.2537,  # specifc heat ratio
        "R": 518.3  # J / Kg*K
    }
    conv = {
        'psi_to_pa': 6894.76,  # Pa
    }

    # correcting fuel flowrate
    # setting to 0
    # correcting for fuel pressure from back calculation of pressure drop from protruding rtd. this is very messy...
    #
    df[prefix+'P_M_Fuel_psi_1'] = filter_offset_df(df['P_M_Fuel_psi'])
    df[prefix+'P_M_Fuel_psi_2'] = .0027 * df[prefix+'P_M_Fuel_psi_1'] ** 2 + .478 * df[prefix+'P_M_Fuel_psi_1']
    df[prefix+'P_M_Fuel_psi_3'] = .0034 * df[prefix+'P_M_Fuel_psi_1'] ** 2 + .4487 * df[prefix+'P_M_Fuel_psi_1']
    df[prefix+'P_M_Fuel_psi'] = df[[prefix+'P_M_Fuel_psi_2', prefix+'P_M_Fuel_psi_3']].mean(axis=1)

    df[prefix+'P_M_Fuel_psia'] = df[prefix+'P_M_Fuel_psi'] + 14.7

    df[prefix+'M_Fuel_Temp_rtd_K'] = df['M_Fuel_Temp_rtd_C']+273
    df[prefix+'M_Fuel_pa_a'] = df[prefix+'P_M_Fuel_psia'] * conv['psi_to_pa']

    # Methane Flowrate
    df[prefix+'m_dot_methane'] = mass_flow_venturi(df, venturi['CD'], venturi['A'], methane['gamma'], prefix+'M_Fuel_pa_a',
                                                  prefix+'M_Fuel_Temp_rtd_K', methane['R'])

    # STOICH Stuff -------------------------------------------------------------------------------------
    fa_stoich = 0.05817
    target_equiv_ratio = .65

    # Fuel air ratio
    mixer = {
        'desc': 'full_power',
        'flow_split': .48,
        'total_cda': .53
    }
    # mixer = {
    #     'desc': 'experimental',
    #     'flow_split': .69,
    #     'total_cda': .53
    # }
    # mixer = {
    #     'desc': 'low_power',
    #     'flow_split': .25,
    #     'total_cda': 1.78
    # }
    df[prefix+'mdot_mixer'] = mixer['flow_split'] * df[prefix+'imp_mf_avg']
    df[prefix+'FA'] = df[prefix+'m_dot_methane'] / df[prefix+'mdot_mixer']
    df[prefix+'stoich_fa_ratio'] = df[prefix+'FA'] ** 0 * fa_stoich
    df[prefix+'FA_overall'] = df[prefix+'m_dot_methane'] / df[prefix+'imp_mf_avg']
    df[prefix+'equiv_ratio'] = df[prefix+'FA'] / fa_stoich
    df[prefix+'target_equiv_ratio'] = df[prefix+'FA'] ** 0 * target_equiv_ratio

    return df
```
