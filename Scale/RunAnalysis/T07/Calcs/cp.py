def cp_calc(p, t):
    # calculate cp from p and t
    # https://www.engineeringtoolbox.com/air-properties-d_156.html
    # return 1.006
    a = 1005.7
    b = 0.1074
    c = -0.0455
    d = 0.00855

    cp = a + b * t + c * t**2 + d * t**3
    cp = cp / 1000
    return cp
