# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:32:02 2016

@author: besser2
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng
#%%

def random_walk(num_steps, num_walkers):
    """
    Generating the random walk data, for statistically
    independent random variables. This for a 2D random walk.

    The two arrays, x and y,
    contain the coordinates of the random walker and the r_sqaured_normal array
    contains the averge displacement of all the walker
    at each time (step number).

    """


    #store distance squared for each walker
    r_squared = np.zeros(num_steps)

    #array to store analytical solutions for the diffusion constant
    diffusion_constant = np.zeros(num_steps)

    # specify all step numbers-- for consistent plotting purposes
    step_num = np.arange(1,num_steps+1)


    plt.figure()
    ax = plt.gca()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis('equal')
    ax.set_title('2D Random Walk:\n\
    %s Steps For Each Walker' %(num_steps),\
    family='monospace',size=12, weight='bold')
    ax.legend("",title='# of Walks= %s' %(num_walkers),loc=1,fontsize=9)


    for j in range(num_walkers):

        # generate random steps +/- 1
        x = ( 2*(rng(num_steps) > 0.5) - 1).cumsum()
        # generate random steps +/- 1
        y = ( 2*(rng(num_steps) > 0.5) - 1).cumsum() # generate random steps +/- 1

        #to get distance_sqaured for each walker
        r_squared_temp = np.add(x**2, y**2)

        # add the distance squared of current walker to last walker
        #this is done for the collection of 2d walks.
        r_squared = r_squared + r_squared_temp


        #plot the coodinates of the random walker after each
        #is generated
        plt.plot(x,y)

    #normalizes the r_squared data
    normal_r_sqaured = r_squared/num_walkers


    #analytically solve for the diffuion
    #all solutions are output in the interactive kernel.
    for i in range(num_steps):
        diffusion_constant[i] = normal_r_sqaured[i]/(2*(i+1))
        print("At Step Number",i+1,":")
        print("Diffusion Constant =", diffusion_constant[i],"\n" )

    plt.show()



    plt.figure()
    ax = plt.gca()
    plt.plot(step_num,normal_r_sqaured,'.')
    plt.xlabel("step number = (time)")
    plt.ylabel("<r$^2$>")
    ax.set_title('2D Random Walk:\n\
    The Average of The Sqaure of the Displacement\n\
    and %s Steps For Each Walker' %(num_steps),\
    family='monospace',size=12, weight='bold')
    ax.legend("",title='# of Walks Averaged= %s' %(num_walkers),loc=2,fontsize=9)
    plt.show()


    return diffusion_constant, normal_r_sqaured



#%%



#%%
def triangle_lattice_random_walk(num_steps, num_walkers):
    """
    Generating the random walk data, for statistically
    independent random variables. This is for a 2D random walk
    on a triangular lattice.

    The two arrays, x_arrray and y_array,
    contain the coordinates of the random walker and the r_sqaured_normal array
    contains the averge displacement of all the walker
    at each time (step number).

    """
    #store distance squared for each walker
    r_squared = np.zeros(num_steps)

    #array to store analytical solutions for the diffusion constant
    diffusion_constant = np.zeros(num_steps)

    # specify all step numbers-- for consistent plotting purposes
    step_num = np.arange(1,num_steps+1)

    #becuase triangular lattice has locations it can move
    #(non-binary arguments).
    #So, creating arrays to store coordinates of the walks
    x_array =np.zeros(num_steps)
    y_array =np.zeros(num_steps)

    plt.figure()
    ax = plt.gca()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis('equal')
    ax.set_title('2D Triangular Lattice: Random Walk\n\
    %s Steps For Each Walker' %(num_steps),\
    family='monospace',size=12, weight='bold')
    ax.legend("",title='# of Walks= %s' %(num_walkers),loc=1,fontsize=9)
    for j in range(num_walkers):

        #evenly distributed values from (0,1]
        theta_step = (rng(num_steps))

        # generate random steps
        #6 possible movement locations for each step
        #So, each condition (excluding the error condition)
        #represents the movement possiblites.
        #AAND the probability that the walk moves in a direction
        #is the same for all six possibilites
        for i in range(num_steps):
            if 0<= theta_step[i] < 1/6:
                x_array[i]=1
                y_array[i]=0

            elif 1/6<= theta_step[i] < 2/6:
                x_array[i]=0.5
                y_array[i]=1


            elif 2/6<= theta_step[i] < 3/6:
                x_array[i]=-0.5
                y_array[i]=1


            elif 3/6<= theta_step[i] < 4/6:
                x_array[i]=-1
                y_array[i]=0


            elif 4/6<= theta_step[i] < 5/6:
                x_array[i]=-0.5
                y_array[i]=-1


            elif 5/6<= theta_step[i] < 1:
                x_array[i]=0.5
                y_array[i]=-1

            else :
                print("Something went wrong")

        cum_x = np.cumsum(x_array)
        cum_y = np.cumsum(y_array)


        #to get distance_sqaured for each walker
        r_squared_temp = np.add(cum_x**2, cum_y**2)

        # add the distance squared of current walker to last walker
        #this is done for the collection of 2d walks.
        r_squared = r_squared + r_squared_temp

        plt.plot(cum_x,cum_y)

    #normalizes the r_squared data
    normal_r_sqaured = r_squared/num_walkers


    #analytically solve for the diffuion
    #all solutions are output in the interactive kernel.
    for i in range(num_steps):
        diffusion_constant[i] = normal_r_sqaured[i]/(2*(i+1))
        print("At Step Number",i+1,":")
        print("Diffusion Constant =", diffusion_constant[i],"\n" )

    plt.show()


    plt.figure()
    ax = plt.gca()
    plt.plot(step_num,normal_r_sqaured,'.')
    plt.xlabel("step number = (time)")
    plt.ylabel("<r$^2$>")
    ax.set_title('2D Triangular Lattice:\n\
    The Average of The Sqaure of the Displacement:\n\
    %s Steps For Each Walker' %(num_steps),\
    family='monospace',size=12, weight='bold')
    ax.legend("",title='# of Walks Averaged= %s' %(num_walkers),loc=2,fontsize=9)
    plt.show()


    return diffusion_constant, normal_r_sqaured





#%%


diffusion1,normal_r_squared1 =  random_walk(num_steps=40, num_walkers=80)
diffusion2,normal_r_squared2 =  random_walk(num_steps=500, num_walkers=1000)

diffusion1_tri,normal_r_squared1_tri= triangle_lattice_random_walk(num_steps=40, num_walkers=80)
diffusion2_tri,normal_r_squared2_tri= triangle_lattice_random_walk(num_steps=500, num_walkers=1000)
