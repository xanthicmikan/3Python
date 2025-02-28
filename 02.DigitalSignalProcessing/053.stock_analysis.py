import numpy as np
import csv
import scipy.signal as signal
import matplotlib.pyplot as plt

csvDataFile = open( 'test.csv' )
reader = csv.reader( csvDataFile )

data = []
for row in reader:
    data.append( row[2] )

price = []
for i in range( 1, len( data ) ):
    price.append( eval( data[i] ) )

day = np.arange( len( price ) )
x = np.array( price )

b1 = np.ones( 5 )/5
y1 = signal.lfilter ( b1, 1, x )

b2 = np.ones( 20 )/20
y2 = signal.lfilter ( b2, 1, x )

plt.figure( 1 )
plt.subplot(131)
plt.plot( day, x, '-', fillstyle = 'bottom' )
plt.xlabel( 'Day' )
plt.ylabel( 'Price' )
plt.axis( [ 0, len( price), 800, 1200] )

plt.subplot(132)
plt.plot( day, x, '--', day, y1, '-' )
plt.xlabel( 'week' )
plt.ylabel( 'Price' )
plt.axis( [ 0, len( price), 800, 1200] )

plt.subplot(133)
plt.plot( day, x, '--', day, y2, '-' )
plt.xlabel( 'Month' )
plt.ylabel( 'Price' )
plt.axis( [ 0, len( price), 800, 1200] )

plt.show()