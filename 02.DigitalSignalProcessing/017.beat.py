import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,1,1000,endpoint = False)

f1=20
f2=200
x=np.cos(2*np.pi*f1*t)*np.cos(2*np.pi*f2*t)
envelop1=np.cos(2*np.pi*f1*t)
envelop2=-np.cos(2*np.pi*f1*t)

plt.plot(t, x, '-')
plt.plot(t, envelop1, '--', color='b')
plt.plot(t, envelop2, '--', color='b')
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')
plt.axis([0,0.1,-1,1])

plt.show()