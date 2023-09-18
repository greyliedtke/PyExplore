"""
Script to call pid loop and prevent value from changing by too much
"""

from simple_pid import PID

# ------------------------------------------------------
# Class for creating pid controller with clamping abilities
class PID_CTRL:
    def __init__(self, p, i, d, sample_time, max_inc, max_dec, setpoint):
        self.pid = PID(p, i, d, setpoint=setpoint, sample_time=sample_time, output_limits=(0,100))
        self.max_inc = max_inc
        self.max_dec = max_dec
        self.prev_ao = 0
        self.prev_n2 = 0

    def limit_acc(self, new_ao, n2_val):
        # preventing acceleration of greater than x
        n2d = n2_val - self.prev_n2
        self.pid.set_auto_mode(enabled=True, l)



    def loop(self, n2_val, prev_ao):
        n2_val, prev_ao = float(n2_val), float(prev_ao)
        new_ao = self.pid(n2_val)

        # clamping new value from being more than max change setting
        if new_ao > prev_ao:
            new_ao = min(prev_ao+self.max_inc, new_ao)
        else:
            new_ao = max(prev_ao-self.max_dec, new_ao)

        return new_ao

    def set_params(self, pd: dict):
        self.pid.tunings = (float(pd["cv_pid_p"]), float(pd["cv_pid_i"]), float(pd["cv_pid_d"]))
        self.max_inc = float(pd["cc_max_inc"])
        self.max_dec = float(pd["cc_max_dec"])
        
# ------------------------------------------------------

# ------------------------------------------------------
# Creating pid functions for control
pid_n2 = PID_CTRL(2, .1, 0, .5, 1, 2, 20)

