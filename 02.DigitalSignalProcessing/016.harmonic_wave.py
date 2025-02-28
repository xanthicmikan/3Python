import numpy as np
import wave
import struct

file = "harmonic.wav"

f1 = 100
amplitude = 10000
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
x1=amplitude*np.cos(2*np.pi*f1*t)
x2=amplitude*np.cos(2*np.pi*(2*f1)*t)
x = x1+x2

np.clip(x, -32768, 32767)

wav_file = wave.open(file, 'w')
wav_file.setparams((num_channels, sampwidth, fs, num_frames, cometype, compname))

for s in x:
    wav_file.writeframes(struct.pack('h',int(s)))
    
wav_file.close()