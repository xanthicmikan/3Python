import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

t=np.linspace(0,5,1000,endpoint = False)

x=signal.chirp(t,0,5,5,'linear')

plt.plot(t, x)
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')
plt.axis([0,5,-1.5,1.5])

plt.show()