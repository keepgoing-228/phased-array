import numpy as np
import math
import matplotlib.pyplot as plt

# Wavelength (cm)
l = 2.4
# Transmitters Interval (cm)
d = 1
# Number of Transmitters
no_elements = 8

# Sample points
theta = np.array([[math.pi*i/180 for i in range(0, 360)]])
n = np.array(range(1, no_elements+1)).reshape(no_elements, 1)

# Phase shift
phaseshift = 0.25*math.pi

# Phased Array Equation
A = (n-1)*(1j*(2*math.pi*d*np.cos(theta)/l + phaseshift))
X = np.exp(-A)
w = np.mat(np.ones(no_elements).reshape(1, no_elements))
r = w*X
r = np.array(np.abs(r)).reshape(-1)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta.reshape(360), np.abs(r).reshape(360))
ax.grid(True)
ax.set_title("Gain of a Uniform Linear Array", va='bottom')
plt.show()
