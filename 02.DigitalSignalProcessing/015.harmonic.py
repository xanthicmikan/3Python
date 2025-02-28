import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,1,1000,endpoint = False)

f1=2
x1=np.cos(2*np.pi*f1*t)
x2=np.cos(2*np.pi*2*f1*t)
x=x1+x2

plt.figure(1)
plt.plot(t, x1)
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')
plt.axis([0,1,-1.2,1.2])

plt.figure(2)
plt.plot(t, x2)
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')
plt.axis([0,1,-1.2,1.2])

plt.figure(3)
plt.plot(t, x)
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')
plt.axis([0,1,-1.2,1.2])

plt.show()