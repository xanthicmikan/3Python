import numpy as np
import wave
from scipy.io import wavfile
import struct
import scipy.signal as signal
import matplotlib.pyplot as plt

infile  = input("Input File: ")   
fs, x = wavfile.read(infile)  
f, t, Zxx = signal.spectrogram( x, fs )

plt.pcolormesh( t, f, abs( Zxx ) )
plt.xlabel( 'Time(Second)' )
plt.ylabel( 'Frequency(Hz)' )

plt.show( )