Here's the Mermaid diagram with colored wiring:

- [batteries](batteries)

```mermaid
graph TD;
    A[Battery] -->|Power| B[Power Management System]
    B -->|Control Signals| C[Screen Controller]
    C -->|Data| D[Screen]
    B -->|Control Signals| E[Microcontroller]
    E -->|Data| D
    style A fill:#f9f,stroke:#333,stroke-width:2px;
    style B fill:#9f9,stroke:#333,stroke-width:2px;
    style C fill:#6ff,stroke:#333,stroke-width:2px;
    style D fill:#9ff,stroke:#333,stroke-width:2px;
    style E fill:#6f9,stroke:#333,stroke-width:2px;
```

```mermaid
graph TD;
    USB --> Charger --- Battery
    Charger --- Pico
    Pico --> Matrix
    Charger --> Matrix
    Pico --> Encoder_1
    Pico --> Encoder_2
    
```


In this diagram:
- **Battery** has a light pink fill color (#f9f).
- **Power Management System** has a light green fill color (#9f9).
- **Screen Controller** has a light blue fill color (#6ff).
- **Screen** has a light cyan fill color (#9ff).
- **Microcontroller** has a light greenish-blue fill color (#6f9).

Feel free to adjust the colors and styles as needed to match your design preferences! Let me know if you need any further customization.