# Calculations


### massflow

        imp_area = 0.00314411  # m^2
        imp_area_factor = 0.9  # impeller af
        bm_area = 3.14159 * (5 * 0.0254) ** 2 / 4  # m^2
        bm_area_factor = 0.90  # bm af


### Recuperator

$$ eff = (Tco-Tci)/(Thi-Tci) $$

Thi: EGT or recuperator LP inlet temp 
Tco: combustor inlet temperature / recuperator HP outlet temp
Tci: recuperator HP inlet temp / PT outlet temp

$$ eff=(Ch*(Thi-Tho))/(Cmin*(Thi-Tci)) $$

Ch: Cp (at Th-ave = (Thi+Tho)/2) * LP side massflow (should be roughly 1.01x HP side massflow)
Cmin: Cp (at Tc-ave = (Tci+Tco)/2) * HP side massflow
Tho: recuperator LP exhaust (if you measure this)

### Engine Cycle

### Models

$$ PR = 0.088 * kW + 1.33 $$
$$ N2 = 0.7 * kW + 24 $$
