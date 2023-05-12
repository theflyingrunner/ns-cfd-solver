import numpy
from matplotlib import pyplot

# Define evenly spaced domain of points 2 units of length wide
nx = 41 # number of grid points
dx = 2 / (nx-1) # distance between any two adjacent points
nt = 25 # number of timesteps
dt = 0.025 # time increment