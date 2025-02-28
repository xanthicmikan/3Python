import numpy as np
import matplotlib.pyplot as plt

N = eval(input("Please enter number of terms of partial sum:"))

t = np.linspace(-1, 1, 1000) #define time array
x = np.zeros(1000) #square's Fourier Series
for n in range(1, N+1):
    x += 2/(n*np.pi)*(1-np.power(-1,n))*np.sin(n*np.pi*t)

plt.plot(t, x)
plt.xlabel('t(sec)')
plt.ylabel('Amplitude')

plt.show()