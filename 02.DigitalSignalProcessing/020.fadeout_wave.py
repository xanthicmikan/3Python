import numpy as np
import wave
import struct

file = "fadeout.wav"

amplitude = 30000
frequency = 300
duration = 10
fs = 44100

num_samples = duration * fs
num_channels = 1
sampwidth = 2
num_frames = num_samples
cometype = "NONE"
compname = "not compressed"

t=np.linspace(0, duration, num_samples,endpoint = False)
a=np.linspace(1, 0, num_samples,endpoint = False)
x=amplitude*a*np.cos(2*np.pi*frequency*t)

wav_file = wave.open(file, 'w')
wav_file.setparams((num_channels, sampwidth, fs, num_frames, cometype, compname))

for s in x:
    #int data--> 16bits
    wav_file.writeframes(struct.pack('h',int(s)))
    
wav_file.close()