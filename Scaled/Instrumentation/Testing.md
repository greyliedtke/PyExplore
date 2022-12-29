# Control Testing Plan

## Airforce

- Non-recuperated
  - passive testing lightoff
    - in progress
  - passive testing full instrumented
    - all instrumentation
      - pressure boards
    - testing improvements
      - improve fuel and oil carts
      - automated air start
      - PID speed control
    - Responding to load changes
- Recuperated
  - Initial testing
    - additional instrumentation
      - ???
    - operational changes
      - braking resistor shutdown
      - blow off valve shutdown
- Regulated
  - Drivetek approach
    - set speed
    - constant power draw
    - slowly increase fuel
    - lose 
  - OCC approach
    - common mode choke?
    - bring engine to idle
    - pid at speed
    - slowly increase load


## Regulated test

- OCC
  - Procedure
    - charge dc bus
    - braking load engaged
    - idle engine
    - enable pid control
    - remove braking load
    - slowly increase regulated load
  - concerns
    - noisy n2 signal
      - 2nd banner?
    - rectifier/inverter tripping
      - how to identify and shut down safely
- DT
  - spin up to xx krpm
  - OCC PSU stabilize dc bus
  - pull load off inverter
  - start engine
  - increase fuel manually
    - dt mechanical power should decrease
    - instrumentation to prove at power level?
  - concerns
    - DT tripping
      - engage braking resistors immediately
      - 

## Calfire

New control system consists of:
- 2 driveteks
- battery system
- 2 turbines

#### Subsytem testing

- custom control of drivetek unit
  - generator and stand for spinning
  - instrumentation
    - banner, PI, drivetek, control computer
  - controls
    - send speed/torque commands
- repeat above with 2 driveteks
  - verify commands, shutdown, noise, errors, comparison
- testing with
