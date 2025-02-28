import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

M = 65
w1 = signal.windows.boxcar( M )
w2 = signal.windows.hamming( M )
w3 = signal.windows.hann( M )
w4 = signal.windows.bartlett( M )
w5 = signal.windows.barthann( M )
w6 = signal.windows.kaiser( M, 14 )

plt.subplot(231)
plt.plot( w1 )
plt.xlabel( 'n (rectangular, boxcar)' )
plt.ylabel( 'Amplitude' )

plt.subplot(232)
plt.plot( w2 )
plt.xlabel( 'n (hamming)' )
plt.ylabel( 'Amplitude' )

plt.subplot(233)
plt.plot( w3 )
plt.xlabel( 'n (hanning)' )
plt.ylabel( 'Amplitude' )

plt.subplot(234)
plt.plot( w4 )
plt.xlabel( 'n (bartlett)' )
plt.ylabel( 'Amplitude' )

plt.subplot(235)
plt.plot( w5 )
plt.xlabel( 'n (blackman)' )
plt.ylabel( 'Amplitude' )

plt.subplot(236)
plt.plot( w6 )
plt.xlabel( 'n (kaiser)' )
plt.ylabel( 'Amplitude' )

plt.show( )