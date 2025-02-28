import numpy as np
import wave
import struct
import scipy.signal as signal
from scipy.io.wavfile import read, write

def downsampling(x, method = 1):
    N = int(len(x)/2)
    y = np.zeros(N)

    if method ==1 : #Decimation
        for n in range(N):
            y[n]=x[2*n]
    else: #Average
        for n in range(N):
            y[n]=(x[2*n]+x[2*n+1])/2
    return y

def upsampling(x, method = 1):
    N = len(x)*2
    y = np.zeros(N)

    if method ==1 : #Zero-order Hold
        for n in range(N):
            y[n]=x[int(n/2)]
    else: #Linear Interpolation
        for n in range(N):
            if int(n/2)==n/2:
                y[n]=x[int(n/2)]
            else:
                n1=int(n/2)
                n2=n1+1
                if n2 <len(x):
                    y[n]=(x[n1]+x[n2])/2
                else:
                    y[n]=x[n1]/2
    return y

def resampling(x, sampling_rate):
    num = int(len(x)*sampling_rate)
    y = signal.resample(x, num)
    return y

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

    print("Sampling Rate Conversion")
    print("1)Downsampling by 2(Decimation)")
    print("2)Downsampling by 2(Average)")
    print("3)Upsampling by 2(Zero-order Hold)")
    print("4)Upsampling by 2(Linear Interpolation)")
    print("5)Resampling")
    choice=eval(input("Please enter your choice:"))

    if choice==1:
        y=downsampling(x,1)
    elif choice==2:
        y=downsampling(x,2)
    elif choice==3:
        y=upsampling(x,1)
    elif choice==4:
        y=upsampling(x,2)
    elif choice==5:
        sampling_rate=eval(input("Sampling Rate="))
        y=resampling(x,sampling_rate)
    else:
        print("Your choice is not supported...")
        y = x

    num_frames=len(y)

    wav_file= wave.open(Outfile, 'w')
    wav_file.setparams((num_channels, sampwidth, fs, num_frames, cometype, compname))
    for s in y:
        wav_file.writeframes(struct.pack('h',int(s)))

    wav_file.close()

main()