import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

fs = 200
t = np.linspace( 0, 1, fs, endpoint = False )
x = np.exp( -t ) * np.sin( 2 * np.pi * 5 * t )
x = np.pad( x, ( 0, fs * 4 ), 'constant' )

b = np.array( [ 1 ] )

num_echos = 5
a = np.zeros( fs * num_echos )
for i in range( num_echos ):
    a[i * fs] = 1 - i / num_echos

y = signal.lfilter( x, b, a )

plt.figure( 1 )
plt.plot( x )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.figure( 2 )
plt.plot( y )
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.show( )