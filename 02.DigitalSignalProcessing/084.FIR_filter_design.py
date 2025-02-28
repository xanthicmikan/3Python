import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

print("FIR filter design using the window method")
print("(1)Lowpass Filter")
print("(2)Highpass Filter")
print("(3)Bandpass Filter")
print("(4)Bandstoppass Filter")
filter = eval(input("Please choose filter :"))
print("------------------------------------")
if filter==1 or filter==2:
    cutoff = eval(input("Enter cutoff frequency(Hz):"))#fc=250
elif filter==3 or filter==4:
    f1 = eval(input("Enter 1st frequency(Hz):"))#f1=200
    f2 = eval(input("Enter 2nd frequency(Hz):"))#f2=300
else:
    print("Not support")
    quit()

n = eval(input("Enter number of taps:"))#31
freq = eval(input("Enter sampling frequency(Hz):"))#1000
print("------------------------------------")
print("Window function")
print("(1)Boxcar")
print("(2)Hamming")
print("(3)Hanning")
print("(4)Bartlett")
print("(5)Blackman")
print("(6)Kaiser")
choice = eval(input("Please choose window type : "))

if choice==1:
    win = 'boxcar'
elif choice==2:
    win = 'hamming'
elif choice==3:
    win = 'hanning'
elif choice==4:
    win = 'hartlett'
elif choice==5:
    win = 'blackman'
elif choice==6:
    win = ('kaiser', 14)
else:
    print("Not support")
    quit()

if filter == 1:
    h = signal.firwin( n, cutoff, window = win, pass_zero = True, fs = freq )
elif filter==2:
    h = signal.firwin( n, cutoff, window = win, pass_zero = False, fs = freq )
elif filter==3:
    h = signal.firwin( n, [f1, f2], window = win, pass_zero = False, fs = freq )
else:
    h = signal.firwin( n, [f1, f2], window = win, pass_zero = True, fs = freq )

w, H =signal.freqz(h)
magnitude = abs(H)
phase = np.angle(H)

plt.figure(1)
plt.plot(w, magnitude)
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Magnitude' )

plt.figure(2)
plt.plot(w, phase)
plt.xlabel( r'$\omega$' )
plt.ylabel( 'Phase' )

plt.show( )