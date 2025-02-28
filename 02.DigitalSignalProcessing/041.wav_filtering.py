import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
import scipy.signal as signal

def average_filtering(x, filter_size):
    h=np.ones(filter_size)/filter_size
    y = np.convolve(x, h, 'same')
    return y

def gauss_filtering(x, sigma):
    filter_size=6*sigma+1
    gauss=signal.windows.gaussian(filter_size, sigma)
    sum=np.sum(gauss)
    gauss=gauss/sum
    y=np.convolve(x,gauss,'same')
    return y

def normalization(x, maximum):
    x_abs=abs(x)
    max_value=max(x_abs)
    y=x/max_value*maximum
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

    print("Filtering")
    print("1)Average Filtering")
    print("2)Gaussian Filtering")

    choice=eval(input("Please enter your choice:"))

    if choice==1:
        filter_size=eval(input("filter size ="))
        y=average_filtering(x,filter_size)
    elif choice==2:
        sigma=eval(input("sigma ="))
        y=gauss_filtering(x,sigma)
    else:
        print("Your choice is not supported...")
        y = x
        
    y=normalization(x,30000)

    wav_file= wave.open(Outfile, 'w')
    wav_file.setparams((num_channels, sampwidth, fs, num_frames, cometype, compname))
    for s in y:
        wav_file.writeframes(struct.pack('h',int(s)))

    wav_file.close()

main()