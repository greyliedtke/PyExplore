"""
handling load following interface

1. Get to idle running condition
2. Lock in on PR, adjust setpoint from PSU reading
3. If out of range / instable

"""

# pressure ratio setpoint

class LoadFollowing:
    def __init__(self):
        self.rate = 0
        self.power = 1.5
        self.ll = 1
        self.kw_regen = 0
        self.kw_load = 0
        self.pr_level = 0
        self.pr_setpoint = 0
        self.mode = 0   # 0 - Manual, 1 - PR Setpoint, 2 - PR adjusted load

    def control_loop(self):
        # control to PR setpoint
        if self.mode == 0:
    
    def pr_adjust(self)
        
