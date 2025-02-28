#x[n]               | x[n]
#1 2 1 2 1 0 0 0 0  |1 2 1 2 1
#1 2 1 2 1
#R[0]=1‧(1)+2‧(2)+1‧(1)+2‧(2)+1‧(1)=11
#
#1 2 1 2 1 0 0 0 0  |1 2 1 2 1
#  1 2 1 2 1
#R[1]=2‧(1)+1‧(2)+2‧(1)+1‧(2)+0‧(1)=8
#
import numpy as np

def autocorr(x):
    R=np.correlate(x,x,'full')
    return R[int(R.size/2):]

def main():
    x = np.array([1,2,1,2,1])
    R = autocorr(x)
    print("x=", x)
    print("Autocorrelate =", R)

main()