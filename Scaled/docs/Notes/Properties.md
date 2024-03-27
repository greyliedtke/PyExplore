# Engineering Properties

# ml /min to gph
h2232_lm = .016
h2232_kgs = h2232_lm * (.817/60)
h2232_gph = h2232_lm * (60/3.78541)

$P*V=n*R*T$

### Equation
```python
def cp_calc(p, t):
    # calculate cp from p and t
    # https://www.engineeringtoolbox.com/air-properties-d_156.html
    # return 1.006
    a = 1005.7
    b = .1074
    c = -.0455
    d = .00855

    cp = a + b*t + c*t**2 + d*t**3
    cp = cp/1000
    return cp
```
