import numpy as np
import wave
import struct
import scipy.signal as signal

file = "triangle.wav"

amplitude = 3000
frequency = 100
duration = 3
fs = 44100

num_samples = duration * fs
num_channels = 1
sampwidth = 2
num_frames = num_samples
cometype = "NONE"
compname = "not compressed"

t=np.linspace(0, duration, num_samples,endpoint = False)
x=amplitude*signal.sawtooth(2*np.pi*frequency*t, 0.5)

wav_file = wave.open(file, 'w')
wav_file.setparams((num_channels, sampwidth, fs, num_frames, cometype, compname))

for s in x:
    wav_file.writeframes(struct.pack('h',int(s)))
    
wav_file.close()