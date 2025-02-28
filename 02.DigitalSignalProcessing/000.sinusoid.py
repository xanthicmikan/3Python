'''
If "No module named numpy" or "matplotlib"
step1: python -m pip install --upgrade pip
step2: pip install numpy
step2: pip install matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000, endpoint = False)
x = np.cos(2*np.pi*5*t)
plt.plot(t, x)
plt.xlabel('t(second)')
plt.ylabel('Amplitude')

plt.show()