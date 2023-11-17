"""
class to handle load ramping 
"""


class LoadMan():
    def __init__(self) -> None:
        self.n2 = 0
        self.sp_n2 = 0
        self.pwr = 0
        self.pwr_sp = 0
        self.psu = 0
        self.psul = 0

        self.state_sp = 5
        self.state = 0
    
    def loop():
        # update all values for state machine

        # if all setpoints reached proceed to next state

    def next_state(self):
        if self.state <= self.state_sp:
            new_sps = 8
            # read new setpoint from dataframe
            
        
