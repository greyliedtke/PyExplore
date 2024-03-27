# PressureRatio

### Engine Notes
- T05
  - PLC handled internally
- NGC
  - PLC Absolute reference I believe?

### Equation
```python
def pressure_ratio(p_pt):
    pr = (p_pt + 101.325) / 101.325
    return pr
```
