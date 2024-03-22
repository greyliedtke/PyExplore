
# Diagrams
## [Drawio](https://drawio-app.com/blog/import-from-csv-to-drawio/)
great tool for quick diagrams and vscode supported
## [Excalidraw](https://excalidraw.com/)
Amazing browser based diagraming
## Mermaid
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