# Leakage

### Engine Notes


### Equation
```python
# ------------------- Leakage -----------------------------------------
def leakage(t_pt_duct, t_pt_exit, t_bypass):
    # function to calculate leakage percent only from temperatures
    mdot = ((t_pt_duct-t_pt_exit) / (t_bypass-t_pt_exit))*100
    return mdot
```
