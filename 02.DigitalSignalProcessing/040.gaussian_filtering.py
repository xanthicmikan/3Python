import numpy as np
import numpy.random as random
import scipy.signal as signal
import matplotlib.pyplot as plt


t = np.linspace(0, 1, 200, endpoint = False)
x = 10*np.cos(2*np.pi*5*t)+random.uniform(-5,5,200)

sigma=3
filter_size=6*sigma+1
gauss=signal.windows.gaussian(filter_size, sigma)#notice "signal.gaussian"-->"signal.windows.gaussian"
sum=np.sum(gauss)
gauss=gauss/sum

y=np.convolve(x,gauss,'same')

plt.figure(1)
plt.plot(t, x)
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')

plt.figure(2)
plt.plot(t, y)
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')

plt.show()