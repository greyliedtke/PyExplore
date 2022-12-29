# 12/20 Work

## Things to work on

- [x] control page updates

- [ ] sheet for part no's
- [ ] Calfire instrumentation order
   - [x] Thermoboard
   - [ ] Pressure Sensors
- [x] Drivetek node guarding email
- [ ] Common mode choke
  - [x] NGC questions email
  - [ ] figure out greg's equations
  - [ ] independent research


## PI Thermocouple board

[ThermoBoard](https://pi-plates.com/thermoplate-users-guide/)
- 8 channels, k type, PI attachment

Planned code

        # imports
        import piplates.THERMOplate as THERMO

        # defaults to k type thermocouples
        THERMO.getTEMP(0,1) # board adress and temp input

        # loop through temps and print out
        tc_s = [0, 1, 2, 3, 4, 5, 6, 7]
        temps = []
        for t in tc_s:
            temps.append(THERMO.getTEMP(0,1))