# Calfire Battery Testing


## Instrumentation
- breaker
- t-slot box

## TIMELINE

## TODO 
- Build Battery frame
  - Wheels?
  - Enclosure?
- Connex
  - Order
  - ???
- Controls
  - Computer
  - DAQ Devices?


## Process

1. Charge each pack to 102.4V using the HV PSU (3.20Vpc)
2. Build a frame to hold the battery packs.
3. Electrically connect the three packs in series using AWG-2 wire
   1. McMaster...?
4. Connect the packs to a 125A 500V 2-pole breaker. This is the electrical interface for the assembled battery.
   1. Order

## Acceptance Testing

1. Charge to 113.6v
   - charging specs?
  
2. Discharge to 91.2v 
    - should be at .3 C which is 30 amps
    - put 3.3 ohms across battery to Discharge
    - measure voltage and current through process.
      - utilize load bank board


### MVP

1. Charge each pack to 102.4V using the HV PSU (3.20Vpc)
2. Build a frame to hold the battery packs.
3. Electrically connect the three packs in series using AWG-2 wire
4. Connect the packs to a 125A 500V 2-pole breaker. This is the electrical interface for the assembled battery.
 

For proper acceptance testing, we should full charge to 113.6V (3.55Vpc) and then discharge to 91.2V (2.85Vpc) to measure the capacity. Discharge should be at ~0.3C, which is ~30A. So we want to put ~3.3Ohms across the battery (with a switch) and dissipate ~3kW. Three of the big 10Ohm power resistors in parallel will work fine. And we want to monitor the voltage and current over the test. The test should take ~3hrs per pack.

After discharge, we would charge back to 102.4Vdc (3.20Vpc)

Our operating voltage range for the full battery will be 290Vdc (3.00Vpc) to 331.2Vdc (3.45Vpc).

We also should understand how to listen to the BMS (we don’t need to talk to it). But we need more information from GreenCubes for that.

The battery pack will slowly self discharge and when the voltage gets too low, permanent damage can occur. So I would strongly ask that we be left to look after the battery, rather than just leaving it somewhere in CA.
