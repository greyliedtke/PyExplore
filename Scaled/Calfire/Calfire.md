


## Instrumentation

### Critical
- accleration
- speeds
- PT exit
- Turbine Exit
- BM inlet

Summary
HSC - 3
NTC -2 
TC - 8
AI - 10
PWM_O - 1


Temperature
- using pi board with 8 TC inputs on each



## Story diagram

1. Driveteks ramp to 20krpm
::: mermaid
    flowchart LR
    Batt(365v Battery)
    DT_01(Drivetek)
    DT_02(Drivetek)
    E_01(Engine 1)
    E_02(Engine 2)

    Batt --> DT_01 --speed---> E_01
    Batt --> DT_02 --speed---> E_02
:::
2. The power-turbines will act as air blowers 
::: mermaid
    flowchart LR
    HX --> Turbine --> Burner
:::
3. The propane section of the burner will then start to add heat into the cycle. As the heat-exchanger warms
up, the core-turbine will start to produce work, and the high-speed shaft will start to accelerate. As the
gas-turbine starts to produce torque on the power-turbine, the power that the power-electronics needs
to deliver will decrease. Once this reaches zero, the gas-turbines are self-sustaining and idling. 


::: mermaid
sequenceDiagram
    participant Burner
    participant HX
    participant Turbine
    participant DT
    participant Batt

    Note right of Batt: Stage 1 - Starting
    Batt ->> DT: Supply 365v power 
    DT ->> Turbine: N2 at 20krpm <br/> blowing air through system

    Note left of Burner: Stage 2 - Lightoff
    Burner ->> Turbine: propane heat added
    Turbine ->> DT: N1 helps spins N2
    Batt ->> DT: Turbine power draws less from battery
  
    Note left of Burner: Stage 3 - Running
    Burner ->> Turbine: syngas heat
    Turbine -> DT: Held at 20krpm
    DT ->> Batt: charging

    Note left of HX: Stage 4 - Shutdown
    HX ->> Turbine: residual heat
    Turbine ->> DT: Held at 30krpm
    DT ->> Batt: decrease to 0

    Note right of Batt: Stage 5 - Cooldown
    Batt ->> DT: supply power
    DT ->> Turbine: speed reduce to 20 krpm <br/> air cools system
:::


## Diagram
::: mermaid
sequenceDiagram
    participant UI
    participant DT
    participant Battery
    participant E
    participant Burner

    Note left of UI: Stage 1 - Starting
    UI ->> DT: Speed Command 
    Note left of UI: Verify reading speed <br/> everything good

    Note left of UI: Stage 2 - Lightoff
    UI ->> Burner: pilot light 
    Note left of UI: wait for dt_mech power to reach 0
    
    Note left of UI: Stage 3 - Running
    UI ->> DT: increase speed 
    UI ->> Burner: syngas flow 
    UI ->> E: modulate bypass
    DT ->> Battery: monitor power
    
    

    Note right of Batt: Stage 5 - Cooldown
    Batt ->> DT: supply power
    DT ->> Turbine: speed reduce to 20 krpm <br/> air cools system
:::
