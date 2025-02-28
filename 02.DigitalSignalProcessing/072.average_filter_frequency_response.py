import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

filter_size = eval(input("Please enter the filter size: "))# 5 15
h = np.ones(filter_size)/filter_size

w,H = signal.freqz(h)
mag=abs(H)

plt.plot( w, mag)
plt.xlabel( r'$\omega$')
plt.ylabel( 'Magnitude') 

plt.show( )