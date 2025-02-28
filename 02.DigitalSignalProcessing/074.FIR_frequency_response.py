import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Lowpass
b = np.array( [ 0.5, 0.5 ] )
w, H0 = signal.freqz( b )
H0 = abs( H0 )

# Highpass
b = np.array( [ 0.5, -0.5 ] )
w, H1 = signal.freqz( b )
H1 = abs( H1 )

plt.figure(1)
plt.plot( w, H0 )
plt.xlabel( r'$\omega$' +' (lowpass)' )
plt.ylabel( 'Magnitude' )

plt.figure(2)
plt.plot( w, H1 )
plt.xlabel( r'$\omega$' +' (highpass)' )
plt.ylabel( 'Magnitude' )

plt.show( )