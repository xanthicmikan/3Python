import numpy as np
import wave
import struct

file = "beat.wav"

f1=20
f2=200
amplitude = 30000
duration = 10
fs = 44100

num_samples = duration * fs
num_channels = 1
sampwidth = 2
num_frames = num_samples
cometype = "NONE"
compname = "not compressed"

t=np.linspace(0, duration, num_samples,endpoint = False)
x=amplitude*np.cos(2*np.pi*f1*t)*np.cos(2*np.pi*f2*t)

wav_file = wave.open(file, 'w')
wav_file.setparams((num_channels, sampwidth, fs, num_frames, cometype, compname))

for s in x:
    #int data--> 16bits
    wav_file.writeframes(struct.pack('h',int(s)))
    
wav_file.close()