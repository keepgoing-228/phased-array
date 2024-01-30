import numpy as np
import math
import matplotlib.pyplot as plt

# wavelength
l = 8.5
# interval of transmitters (1/2 wavelength is better)
d = 10
# number of transmitters
elements = 8
# phased shift
phaseshift = -0.5*math.pi
# angle of the main wave
theta = np.array([math.pi*i/100 for i in range(0,360)])
N = np.array(range(1,elements+1)).reshape(elements,1)

# phased array equation
A = (N-1)*(-1j*(2*math.pi*d*np.cos(theta)/l + phaseshift)) #(8.360)
X = np.exp(A)
W = np.mat(np.ones(elements).reshape(1,elements)) #(1,8)
r_tatal = W*X  #summation
r_tatal = np.array(np.abs(r_tatal)).reshape(-1) # (1, 360) -> (360, )

# plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta.reshape(360), np.abs(r_tatal).reshape(360))
ax.grid(True)
ax.set_title("Gain of a Uniform Linear Array", va='top')
plt.show()
