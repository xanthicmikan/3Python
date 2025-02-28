import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

sigma = eval(input("Please enter sigma: "))#1 , 3
filter_size=int(6*sigma+1)
gauss=signal.windows.gaussian(filter_size, sigma)
sum=np.sum(gauss)
gauss=gauss/sum

w,H = signal.freqz(gauss)
mag=abs(H)

plt.plot( w, mag)
plt.xlabel( r'$\omega$')
plt.ylabel( 'Magnitude') 

plt.show( )