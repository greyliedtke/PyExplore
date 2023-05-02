import streamlit as st
import pandas as pd
import numpy as np
from audopy import get_amp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

st.title('SoundMan')

fig, ax = plt.subplots()

plen = 60

amp_a = [0]*plen
amp_i = list(range(len(amp_a)))


line, = ax.plot(amp_i, amp_a)
ax.set_ylim([0,1])
the_plot = st.pyplot(plt)

def init():  # give a clean slate to start
    line.set_ydata(amp_a)

def animate():  # update the y values (every 1000ms)
    line.set_ydata(amp_a[-plen:])
    the_plot.pyplot(plt)


f_data, f_count = [], 100
def get_freq():
    # get frequency from past 
    freq_d = amp_a[-f_count:]

    # Compute the Fourier transform of the signal
    fft = np.fft.fft(freq_d)

    # Compute the frequencies corresponding to the Fourier coefficients
    freqs = np.fft.fftfreq(len(freq_d), 1/sample_rate)

    # Find the index of the maximum Fourier coefficient
    max_idx = np.argmax(np.abs(fft))

    # Get the frequency corresponding to the maximum coefficient
    freq = freqs[max_idx]
    print(freq)

sample_rate = 10
init()

f_i = 0

while True:
    # print(amp_a)
    amp_a.append(get_amp())
    animate()

    if f_i>f_count:
        get_freq()
        f_i = 0
    f_i +=1

    time.sleep(1/sample_rate)

