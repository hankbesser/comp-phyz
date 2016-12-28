# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 13:45:43 2016

@author: hbesser
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng
#%%

def random_walk(num_steps, num_walkers):
    """
    Generating the random walk data, for statistically
    independent random variables. This for a 2D random walk.
    
    The two arrays, x_coord and y_coord, 
    contain the coordinates of ALL the random walkers, 
    making it easy to access the a certain position at 
    a specified step number for all the walkers. 
    
    """ 
    # to store x position for all the walkers
    x_coord = np.zeros((num_walkers,num_steps))
    
    # to store y position for all the walkers
    y_coord = np.zeros((num_walkers,num_steps))
    
    
    
    for j in range(num_walkers):
    
        # generate random steps +/- 1
        x = ( 2*(rng(num_steps) > 0.5) - 1).cumsum() 
        # generate random steps +/- 1
        y = ( 2*(rng(num_steps) > 0.5) - 1).cumsum()

        #store data
        x_coord[j,:]=x
        #store data
        y_coord[j,:]=y
    
    #return variables for plotting   
    return x_coord,y_coord,num_steps,num_walkers
    



#%%

def entropy(num_steps,num_walkers,nbins):
    
    """
    
    Finds the entropy of the system (given a specified number
    of steps and walkers)
    
    First: Generating the random walk data, for statistically
    independent random variables..no contraints 
    
    
    Second: given this data, computes the entropy of the system
    by finding the probability that a particle resides in the certain
    part in the sqaure lattice.
    This is done using the grid method (nbins by nbins) where
    the xedges and yedges for the histogram are evenly partioned with
    nbins # of bins.
 
    """ 
    
    #call to the pseudo-instance (i.e the method-like usage of the
    #random walk function)
    x_coord_e,y_coord_e,num_steps_e,num_walkers_e =\
    random_walk(num_steps=num_steps, num_walkers=num_walkers)
    
    #
    xedges = np.linspace(-1*num_steps_e,num_steps_e,nbins+1) 
    yedges = np.linspace(-1*num_steps_e,num_steps_e,nbins+1)
    
    #calaculate entropy at each time step
    Entropy = np.zeros(num_steps_e)
    
    
    
    #Loop: x_coord and y_coord are read at each time-step(num_steps)
    #these values are used to calculate their histograms 
    for s in range(num_steps_e):
        histo=np.histogram2d(x_coord_e[:,s],y_coord_e[:,s],bins=(xedges,yedges))
    
        #probability measure for finding the walkers at position[i,j] in grid    
        prob = histo[0]/sum(sum(histo[0]))
    
        v=0
  
   
        for i in range(nbins):
            for j in range(nbins):
            
                if(prob[i,j]>0):
                    #using the entropy equation
                    v+=-prob[i,j]*np.log(prob[i,j])
                    Entropy[s]=v
    
    #return values for plotting
    return Entropy,x_coord_e,y_coord_e,num_steps_e,num_walkers_e
               

    
#%%
def diffusion_confined_space(num_steps,num_walkers):

    """
    Generating the random walk data, for statistically
    independent random variables. This for a 2D random walk.
    
    The two arrays, x_coord and y_coord, 
    contain only the particles in the
    specified coordinates: contrained to -100 to 100 for both axes
    (i.e 200X200 coordinate system--square lattice). 
    
    """ 
    # to store x position for all the walkers
    x_coord = np.zeros((num_walkers,num_steps))
    
    # to store y position for all the walkers
    y_coord = np.zeros((num_walkers,num_steps))
    
    
    
    for j in range(num_walkers):
    
        # generate random steps +/- 1
        x = ( 2*(rng(num_steps) > 0.5) - 1).cumsum() 
        # generate random steps +/- 1
        y = ( 2*(rng(num_steps) > 0.5) - 1).cumsum()
       
        #store data
        x_coord[j,:]=x
        
        #store data
        y_coord[j,:]=y

    #fills all values outside boundary with np.nan  
    for i in range(num_walkers):
        for j in range (num_steps):
            if 100<x_coord[i,j] or x_coord[i,j]<-100 or\
            100<y_coord[i,j] or y_coord[i,j]<-100: 
                x_coord[i,j] = np.nan
                y_coord[i,j] = np.nan
    
    #return variables for plotting   
    return x_coord,y_coord,num_steps,num_walkers 
    
#%%    
#Entropy and Free Diffusion


entropy,x_coord_free,y_coord_free,num_steps_free,num_walkers_free =\
entropy(num_steps=1700, num_walkers=1000,nbins=64)

#Constrained on 200 X 200 Sqaure Lattice
x_coord_bound,y_coord_bound,num_steps_bound,num_walkers_bound=\
diffusion_confined_space(num_steps=1700,num_walkers=1000)

#%%

#Plots    



plt.figure()
ax = plt.gca()
# Entropy
plt.plot(np.arange(1,num_steps_free+1),entropy)
plt.xlabel("time (number of steps)")
plt.ylabel("Entropy")
ax.set_ylim(bottom=0)
ax.set_title('2D Random Walk-Mixing Cream in Coffee\n\
Entropy versus Time (%s Random-Walk Steps)' %(num_steps_free),\
family='monospace',size=12, weight='bold')
ax.legend("",title='# of Particles (walks)= %s' %(num_walkers_free),loc=2,fontsize=9) 
plt.show    


plt.figure()
ax = plt.gca()
#plot the position of random walkers before the first step
plt.plot(x_coord_free[:,0],y_coord_free[:,0],'o')
plt.xlabel("x")
plt.ylabel("y")
ax.set_xlim(-150,150)
ax.set_ylim(-150,150)
ax.set_title('2D Random Walk-Free Diffusion',\
family='monospace',size=12, weight='bold')
ax.legend("",title='Position at t = %s \n # of Particles (walks)= %s ' %(0,num_walkers_free),loc=1,fontsize=8) 
plt.show



plt.figure()
ax = plt.gca()
#plot the position of random walkers at the num_steps/2 step
plt.plot(x_coord_free[:,int(num_steps_free/2)],y_coord_free[:,int(num_steps_free/2)],'o')
plt.xlabel("x")
plt.ylabel("y")
ax.set_xlim(-150,150)
ax.set_ylim(-150,150)
ax.set_title('2D Random Walk-Free Diffusion',\
family='monospace',size=12, weight='bold')
ax.legend("",title='Position at t = %s \n # of Particles (walks)= %s ' %(int(num_steps_free/2),num_walkers_free),loc=1,fontsize=8) 
plt.show







plt.figure()
ax = plt.gca()
#plot the position of random walkers at the last step
plt.plot(x_coord_free[:,-1],y_coord_free[:,-1],'o')
plt.xlabel("x")
plt.ylabel("y")
ax.set_xlim(-150,150)
ax.set_ylim(-150,150)
ax.set_title('2D Random Walk-Free Diffusion',\
family='monospace',size=12, weight='bold')
ax.legend("",title='Position at t = %s \n # of Particles (walks)= %s ' %(num_steps_free,num_walkers_free),loc=1,fontsize=8) 
plt.show






#%%
#More Plots

plt.figure()
ax = plt.gca()
#plot the position of random walkers before the first step
plt.plot(x_coord_bound[:,0],y_coord_bound[:,0],'o')
plt.xlabel("x")
plt.ylabel("y")
ax.set_xlim(-150,150)
ax.set_ylim(-150,150)
ax.set_title('2D Random Walk-Particles Constrained\n\
Cream in Coffe',\
family='monospace',size=12, weight='bold')
ax.legend("",title='Position at t = %s \n # of Particles (walks)= %s ' %(0,num_walkers_free),loc=1,fontsize=8) 
plt.show








plt.figure()
ax = plt.gca()
#plot the position of random walkers at the num_steps/2 step
plt.plot(x_coord_bound[:,int(num_steps_bound/2)],y_coord_bound[:,int(num_steps_bound/2)],'o')
plt.xlabel("x")
plt.ylabel("y")
ax.set_xlim(-150,150)
ax.set_ylim(-150,150)
ax.set_title('2D Random Walk-Particles Constrained\n\
Cream in Coffe',\
family='monospace',size=12, weight='bold')
ax.legend("",title='Position at t = %s \n # of Particles (walks)= %s ' %(int(num_steps_free/2),num_walkers_free),loc=1,fontsize=8) 
plt.show





plt.figure()
ax = plt.gca()
#plot the position of random walkers at the last step
plt.plot(x_coord_bound[:,-1],y_coord_bound[:,-1],'o')
plt.xlabel("x")
plt.ylabel("y")
ax.set_xlim(-150,150)
ax.set_ylim(-150,150)
ax.set_title('2D Random Walk-Particles Constrained\n\
Cream in Coffe',\
family='monospace',size=12, weight='bold')
ax.legend("",title='Position at t = %s \n # of Particles (walks)= %s ' %(num_steps_free,num_walkers_free),loc=1,fontsize=8) 
plt.show






 
