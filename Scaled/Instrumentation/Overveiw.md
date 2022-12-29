# Instrumentation

### Calfire

- pressure sensors
- tc's
- speed
- acceleration?

### General Format for organizing all instrumentation

- Part No
- description
- software notes
- serialized No

### Uses

- Project use
- description
- excel based...
- readme exportable from project

## Diagram

::: mermaid 
flowchart LR

subgraph 01[Instrumentation Sheet]
    direction LR 
    Serialized_No
    Description
    Part_No
    Link
end

subgraph 02[Project Sheet]
    direction LR 
    SPI_Serialized_No
    Software_Name
end

subgraph 03[Software Sheet]
    direction LR 
    SPI_Serialized_No
    Calibrations
end

01 --serialized_no--> 02 

:::
