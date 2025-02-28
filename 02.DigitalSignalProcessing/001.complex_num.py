import numpy as np

#z = complex(3,4)
z = 3+4j
#|z| = 5
magnitude = abs(z)
#tan-1(4/3)
theta = np.angle(z)*180/np.pi

print("z=",z)
print("Magnitude=",magnitude)
print("Phase Angle=",theta)