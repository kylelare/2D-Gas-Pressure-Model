import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math

nsteps = 100 #Number of steps completed by each random walker
nwalkers = 100 #Number of random-walkers/gas-particles in the system
boxlength = 10 #Length of simulation box

#nwalkers that start at (0,0) and move in any direction for nsteps
xv = []
yv = []
xv.append(0)
yv.append(0)
pistonperparticle = list()
pistoncounttotal = 0
ii = 0
for j in range(nwalkers):
    x = 0
    y = 0
    pistoncount = 0
    for i in range(nsteps):
        #print(ii)
        val = rd.random()  # choose + step or - step
        theta = 2. * math.pi * val  # pick random direction
        x += math.cos(theta)
        y += math.sin(theta)
        while x > .5*boxlength:
            x = x - .1*boxlength
            #print('>x',x)
        while y > .5*boxlength:
            y = y - .1*boxlength
            #print('>x', y)
        while x < -.5*boxlength:
            x = x + .1*boxlength
            #print('<x',x)
        while y < -.5*boxlength:
            y = y + .1*boxlength
            #print('<y',y)
        else:
            ii+=1
            xv.append(x)
            yv.append(y)
        if .9*(.5*boxlength) <= x <= .5*boxlength:  # defining the right wall of the box to be our "piston"
            pistoncounttotal += 1
            pistoncount += 1
    pistonperparticle.append(pistoncount)

plt.plot(pistonperparticle) #Plot of piston counts per particle
#print(pistonperparticle)
plt.xlabel('Particle')
plt.ylabel('Piston Count')
plt.title('Piston Count Per Particle')
plt.xticks(np.arange(0,nwalkers, step =nwalkers/10))
plt.show()

pressureperparticle = list()
for i in pistonperparticle:
    x = float(i)/.005 #simulated pressure in pascals per particle
    pressureperparticle.append(x)
plt.plot(pressureperparticle)
plt.xlabel('Particle')
plt.ylabel('Pressure (Pa)')
plt.title('Pressure Contribution Per Particle')
plt.xticks(np.arange(0,nwalkers, step =nwalkers/10))
plt.show()
#print(pistoncounttotal)

plt.plot(xv,yv) #Plot of paths of all walkers/particles
plt.xlim(-.5*boxlength-.5,.5*boxlength+.5)
plt.ylim(-.5*boxlength-.5,.5*boxlength+.5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Path of Walkers")
plt.show()