import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
from numpy.fft import fft, fftshift, ifft, fftfreq

def spectrum_shifting( x, shift, fs ):
    X = fft( x )
    N = fs
    N_half = int( fs / 2 )
    Y = np.zeros( N, dtype = 'complex' )
    for i in range( N_half ):
        if i + shift >= 0 and i + shift <= N_half:
            Y[i + shift] = X[i]
    for i in range( N_half + 1, fs ):
        if i - shift >= N_half + 1 and i - shift < N:
            Y[i - shift] = X[i]
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

      yy = spectrum_shifting( xx, 500, fs )

      for i in range( iter * N, ( iter + 1 ) * N ):
          if i < x.size:
              y[i] = yy[i - iter * N]

    wav_file = wave.open(outfile,'w')
    wav_file.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname))

    for s in y:
      wav_file.writeframes(struct.pack('h',int(s)))

    wav_file.close( )

main( )