import numpy as np
import wave
import struct
import scipy.signal as signal

file = "sinusoid_echo.wav"

amplitude = 20000
frequency = 200
duration = 5
fs = 44100
num_samples = duration * fs

num_channels = 1
sampwidth = 2
num_frames = num_samples
comptype = "NONE"
compname = "not compressed"

t = np.linspace( 0, 1, fs, endpoint = False )
x = np.exp( -t ) * amplitude * np.sin( 2 * np.pi * frequency * t )
x = np.pad( x, ( 0, 4 * fs ), 'constant' )

b = np.array( [ 1 ] )

a = np.zeros( duration * fs )
num_echos = 5
for i in range( num_echos ):
    a[ int( i * fs * 5 / num_echos ) ] = 1 - i / num_echos

y = signal.lfilter( x, b, a )
y = np.clip( y, -30000, 30000 )

wav_file = wave.open( file, 'w' )
wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname ))

for s in y :
   wav_file.writeframes( struct.pack( 'h', int ( s ) ) )

wav_file.close( )