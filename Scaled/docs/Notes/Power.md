# Power

### Passive Configuration

$P = Voltage^2 / Resistance$
$P = Voltage * Current$
$P = 120 * LL_*.72*$
$Voltage = Speed*Back_EMF$
$Resistance = 10ohm/LL$


### EMF
- T07/NGC
    - 3.48 V/kRPM
- T05
  - 2.55 V/kRPM

### Equation
```python
def power_kw(v1, v2, v3, i1, i2, i3):
    v_avg = (v1+v2+v3)/3
    i_sum = sum([i1,i2,i3])
    return v_avg*i_sum/1000

# T5
voltages = ['generator phase1 voltage', 'generator phase2 voltage', 'generator phase3 voltage']
currents = ['generator phase1 current', 'generator phase2 current', 'generator phase3 current']
va = voltages+currents
df["CV_PLC_Passive_kW"] = ac(power_kw, va, df)

NGC:
["PLC_V_Phase_1_Voltage", "PLC_V_Phase_2_Voltage", "PLC_V_Phase_3_Voltage"]
["PLC_V_Phase_1_Current", "PLC_V_Phase_2_Current", "PLC_V_Phase_3_Current"]
[
        "PLC_V_Phase_1b_Current",
        "PLC_V_Phase_2b_Current",
        "PLC_V_Phase_3b_Current",
    ]
    
"""

```
