



- Dynamics
- Statics
- Fluids
- Statistics
  - [Reference](https://byjus.com/statistics-formulas/)
  - Mean
  - Median
  - Variance
  - Standard Deviation
- Electrical
- Geometry



## Base Units
- The building blocks for dimensions
- The simples physical representation of something
- Combining base units leads to derived dimensions
- 
  
  ::: mermaid
  flowchart LR
    subgraph Equations
    direction LR
    F=M*A
    end
    subgraph Dimensions
    direction LR
    F=M*A--> F_Force
    F=M*A--> M_Mass
    F=M*A--> A_Acceleration
    end
    subgraph Base Units
    direction LR
    F_Force --> L
    F_Force --> M
    F_Force --> T

    M_Mass --> M

    A_Acceleration --> L
    A_Acceleration --> T
    end
:::
