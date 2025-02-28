import numpy as np
import wave
import struct
import scipy.signal as signal
from scipy.io.wavfile import read, write

def AM(x, f ,fs):
    t = np.zeros(len(x))
    for i in range(len(x)):
        t[i]=i/fs
    carrier = np.cos(2*np.pi*f*t)
    return x *carrier

def main():
    infile = input("Input File:")
    Outfile = input("Output File:")

    wav= wave.open(infile, 'rb')
    
    num_channels = wav.getnchannels()
    sampwidth = wav.getsampwidth()
    fs = wav.getframerate()
    num_frames = wav.getnframes()
    cometype = wav.getcomptype()
    compname = wav.getcompname()
    wav.close()
    sampling_rate,x = read(infile)

    fc =eval(input("Please enter carriei frequency(Hz):"))#1000
    y = AM(x, fc, fs)
    
    wav_file= wave.open(Outfile, 'w')
    wav_file.setparams((num_channels, sampwidth, fs, num_frames, cometype, compname))
    for s in y:
        wav_file.writeframes(struct.pack('h',int(s)))

    wav_file.close()

main()