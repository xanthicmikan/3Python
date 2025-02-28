import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

fs = 100
t = np.linspace( 0, 1, fs, endpoint = False )
x1 = np.cos( 2 * np.pi * 10 * t )
x2 = np.cos( 2 * np.pi * 20 * t )
x = x1 + x2

b = np.array( [ 1, -2 * np.cos( 2 * np.pi * 20 / fs ), 1 ] )
y = signal.lfilter( b, 1, x )

plt.subplot(121)
plt.plot( t, x )
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 1, -2, 2 ] )

plt.subplot(122)
plt.plot( t, x1, '--', t, y, '-' )
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )
plt.axis( [ 0, 1, -2, 2 ] )

plt.show()