"""
creating matrix clock
"""

# clock
import keyboard
import time
from datetime import datetime
import MatMap.Mat as mat
import MatMap.setup as pc
from MatMap.Temperature import get_temperature
from MatMap.Mat import characters
import numpy as np

class Scene:
    def __init__(self):
        self.rate = .25
        self.time = "00:00:00"
        self.temp = 20
        self.init_time = time.perf_counter()
        self.time_mat = [[],[]]
        self.sec_mat = [[],[]]
        self.temp_mat = [[],[]]
        self.deg_mat = [[7,7,7,7,8,8],[12,14,3,4,3,4]]

    def init_page(self):
        # slowly draw scene?
        # fill in borders and what not
        # for p in mat.pixel_outline:
        #     strip[p] = pc.color_background
        pass

    def set_sec(self, seconds):
        sec_x, sec_y = [], []
        sec_pixes = mat.seconds_mat[0:seconds]
        for b in sec_pixes:
            mx, my = mat.mat_xy(b)
            sec_x.append(mx)
            sec_y.append(my)
        self.sec_mat = np.column_stack([sec_x, sec_y])


    def set_temp(self):
        # fetch temperature if time passed
        et = time.perf_counter() - temp_time
        if et > pc.temp_refresh:
            temp_time = time.perf_counter()
            try:
                temp = get_temperature()
                # turning temperature vals into tens and ones int
                temp1 = int(temp//10)
                temp2 = int(temp%10)
            except:
                temp = 0
            t1_mx, t1_my = characters[5].char_matrix(temp1)
            t2_mx, t2_my = characters[6].char_matrix(temp2)
            temp_mat = [t1_mx+t2_mx], [t1_my+t2_my]
            self.temp_mat = np.column_stack(temp_mat)
        else:
            pass
        return temp_mat

    def loop(self):
        # get time
        tn = datetime.now().strftime("%H:%M:%S")

        # sending hours and minutes
        mx, my = [], []
        for i, t in enumerate([tn[0], tn[1], tn[3], tn[4]]):
            matrix = characters[i].char_matrix(int(t))
            mx += matrix[0]
            my += matrix[1]

        for i, t in enumerate([2,3]):
            matrix = characters[i+4].char_matrix(int(t))
            mx += matrix[0]
            my += matrix[1]

        for i, t in enumerate([tn[6], tn[7]]):
            matrix = characters[i+6].char_matrix(int(t))
            mx += matrix[0]
            my += matrix[1]

        self.time_mat = np.column_stack([mx, my])
        # self.set_temp()
        # determining seconds to send
        # secs = int(tn[6:8])
        # self.set_sec(secs)

    # def adjust_time(self):    # need for pico...

clock = Scene()
