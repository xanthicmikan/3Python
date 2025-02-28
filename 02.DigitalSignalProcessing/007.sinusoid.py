import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,1,1000,endpoint = False)
x=np.cos(2*np.pi*5*t)

plt.plot(t, x)
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')
plt.axis([0,1,-1.2,1.2])

plt.show()