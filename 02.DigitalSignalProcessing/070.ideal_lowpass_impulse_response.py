import numpy as np
import matplotlib.pyplot as plt

filter_size = eval(input("Please enter the filter size: "))# 5 11 21 31
filter_half = int(filter_size/2)
wc = np.pi / 2

na = np.arange( -filter_half, filter_half + 1 )
h = np.zeros( filter_size )
for n in na:
    if n == 0:
        h[n+filter_half] =  0.5
    else:
        h[n+filter_half] = np.sin( wc * n ) / ( np.pi * n )

plt.stem( na, h)
plt.xlabel('n)')
plt.ylabel('h[n]')

plt.show( )