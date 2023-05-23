import numpy
from matplotlib import pyplot
import time
import sys

def linconv(nx):
    # Define evenly spaced domain of points 2 units of length wide
    # # number of grid points
    dx = 2 / (nx-1) # distance between any two adjacent points
    nt = 25 # number of timesteps
    c = 1 # constant wave speed
    sigma = 0.5
    dt = sigma * dx # time increment

    # and u = 1 everywhere else in x = (0,2)
    u = numpy.ones(nx) # array for speed u
    # set up the initial conditions
    # initial velocity u0 is u = 2 in the interval 0.5 <= x <= 1 
    u[int(0.5 / dx):int(1 / dx + 1)] = 2

    pyplot.plot(numpy.linspace(0,2,nx),u)
    pyplot.show()

    # finite-difference discretization scheme
    # forward difference for time and backward difference for space
    un = numpy.ones(nx) # temp array corresponding to u_i^n+1
    # nested loop to iterate over each time-step, then loop through space
    # applying the formula derived from combining the FD and BD schemes
    for i in range(0,nt):
        un = u.copy() # copy current values in u to un
        for j in range(1,nx):
            u[j] = un[j] - c * dt / dx * (un[j] - un[j-1])

    pyplot.plot(numpy.linspace(0,2,nx),u)
    pyplot.show()
    print("dt = " + str(dt))

linconv(41)