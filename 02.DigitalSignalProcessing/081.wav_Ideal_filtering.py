import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
from numpy.fft import fft, fftshift, ifft, fftfreq

def ideal_lowpass_filtering( x, cutoff, fs ):
    X = fft( x )
    H = np.zeros( fs )
    for i in range( -cutoff, cutoff + 1 ):
        H[i] = 1
    Y = H * X
    y = ifft( Y )
    y = y.real
    return y

def ideal_highpass_filtering( x, cutoff, fs ):
    X = fft( x )
    H = np.zeros( fs )
    for i in range( -cutoff, cutoff + 1 ):
        H[i] = 1
    H = 1 - H
    Y = H * X
    y = ifft( Y )
    y = y.real
    return y

def ideal_bandpass_filtering( x, f1, f2, fs ):
    X = fft( x )
    H = np.zeros( fs )
    for i in range( f1, f2 + 1 ):
        H[i] = 1
    for i in range( -f1, -f2 - 1, -1 ):
        H[i] = 1
    Y = H * X
    y = ifft( Y )
    y = y.real
    return y

def ideal_bandstop_filtering( x, f1, f2, fs ):
    X = fft( x )
    H = np.zeros( fs )
    for i in range( f1, f2 + 1 ):
        H[i] = 1
    for i in range( -f1, -f2 - 1, -1 ):
        H[i] = 1
    H = 1 - H
    Y = H * X
    y = ifft( Y )
    y = y.real
    return y

def ideal_allpass_filtering( x ):
    X = fft( x )
    Y = X
    y = ifft( Y )
    y = y.real
    return y

def main( ):
    infile  = input( "Input File: " )
    outfile = input( "Output File: " )

    wav = wave.open( infile, 'rb' )
    num_channels = wav.getnchannels()
    sampwidth    = wav.getsampwidth()
    fs           = wav.getframerate()
    num_frames   = wav.getnframes()
    comptype     = wav.getcomptype()
    compname     = wav.getcompname()
    wav.close( )

    sampling_rate, x = read(infile)

    y = np.zeros( x.size )
    n = int( x.size / fs ) + 1
    N = fs
    for iter in range( n ):
      xx = np.zeros( N )
      yy = np.zeros( N )
      for i in range( iter * N, ( iter + 1 ) * N ):
          if i < x.size:
              xx[i - iter * N] = x[i]

      yy = ideal_lowpass_filtering( xx, 2000, fs )

      for i in range( iter * N, ( iter + 1 ) * N ):
          if i < x.size:
              y[i] = yy[i - iter * N]

    wav_file = wave.open(outfile,'w')
    wav_file.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname))

    for s in y:
      wav_file.writeframes(struct.pack('h',int(s)))

    wav_file.close( )

main( )
