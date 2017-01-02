"""
Created on Sat Nov  5 11:25:05 2016

@author: hbesser
"""
import matplotlib.pyplot as plt
import numpy as np


#%%


def fixed_ends(dx,l):
    """
    Solution of wave equation for a string
    when both ends are fixed. dx is the grid spacing
    parameter in meters, and l is length of string. Parameter for the wave speed
    is set to 300 m/s in script.
    This is a vectorised version of the code provided.

    There are 3 vectors containing positional information for the system
    y_new, y_current and y_previous. The vectorised version serves as a guide
    to one--clearly understand the the algorithms--
    and two: provides a more effiecient way to to update
    the information.
    """
    #Define Constants
    c = 300    # wave speed in m/s
    dt = dx/c  # time in seconds
    r = c*dt/dx # dimensionless variable r to relate dt and dx to c



    n = int(l/dx) # number of grid points on the string - 1
    #time value of interest
    if n>100:
        n=100

    #preallocate memory for speed
    y_current=np.zeros(n+1)
    y_previous=np.zeros(n+1)
    y_next=np.zeros(n+1)




    # Initialise string position (must exclude the end points in main loop)
    for i in range(n+1):
        y_current[i]= y_previous[i] = np.exp(-1000*(i*dx - 0.3)**2)




    plt.figure()
    ax = plt.gca()
    ax.get_xaxis().set_ticks([])
    ax.set_xlabel("time (au)")
    ax.set_ylabel("displacement (au)")
    ax.set_title('Wave Motion Simulation on a String-With Fixed Ends:\n\
    Wave Displacement at Different Times',\
    family='monospace',size=12, weight='bold')
    ax.legend("",title='dx= %s' %(dx),loc=3)
    for j in range(200):

        #Now specify Boudary conditions-start and end boundries-
        #BECAUSE this is the fixed enpoints example
        y_current[0]=0
        y_previous[0]=0
        y_next[0]=0

        y_current[-1]=0
        y_previous[-1]=0
        y_next[-1]=0

        for i in range(0,n-2):
            #nearest neighbor algorithm
            y_next[i+1]=2*(1-r**2)*y_current[i+1]-\
            y_previous[i+1]+r**2*(y_current[i+2]+y_current[i])


        #creating a series of modulo operators and setting the remainder
        #eqaul to zero  to plot the generated waves
        #at specified rates at specfied generations.
        for i in range(n-2):
            y_previous[i+1]= y_current[i+1]
            y_current[i+1] = y_next[i+1]

        if (j%4 ==0 and j<10):
            plt.plot(y_next[:])

        if  (j%40 ==0 and 5<=j<=95):
            plt.plot(y_next[:])

        if  (j%4 ==0 and 96<=j<=105):
            plt.plot(y_next[:])

        if  (j%40 ==0 and 106<=j<=200):
            plt.plot(y_next[:])


            plt.plot(y_next[:])
    plt.show()

    #stacking the vectors to inpsect the object.
    return np.vstack((y_previous,y_current,y_next))




#%%
def free_ends(dx,l):
    """
    Solution of wave equation for an oscillating string
    when both ends are free. dx is the grid spacing
    parameter in meters, and l is length of string. Parameter for the
    wave speed, c is set to 300 m/s in script.
    This is a vectorised version of the code provided.

    There are 3 vectors containing positional information for the system
    y_new, y_current and y_previous. The vectorised version serves as a guide
    to one--clearly understand the the algorithms--
    and two: provides a more efficient way to understand the updated
    information without using temporary.
    """
    #Define Constants
    c = 300    # wave speed in m/s
    dt = dx/c  # time in seconds
    r = c*dt/dx # dimensionless variable r to relate dt and dx to c



    n = int(l/dx) # number of grid points on the string - 1
    #time value of interest
    if n>100:
        n=100

    #preallocate memory for speed
    y_current=np.zeros(n+1)
    y_previous=np.zeros(n+1)
    y_next=np.zeros(n+1)




    # Initialise string position (must exclude the end points in main loop)
    for i in range(n+1):
        y_current[i]= y_previous[i] = np.exp(-1000*(i*dx - 0.3)**2)




    plt.figure()
    ax = plt.gca()
    ax.get_xaxis().set_ticks([])
    ax.set_xlabel("time (au)")
    ax.set_ylabel("displacement (au)")
    ax.set_title("Wave Motion Simulation on a String-With Free Ends:\n\
    Wave Displacement at Different Times",\
    family='monospace',size=12, weight='bold')
    ax.legend("",title='dx= %s' %(dx),loc=3)
    for j in range(200):
        # ONLY DIFFERENCES from fixed end:
        #No Boundrary condtion defined, INSTEAD,
        #The positions of free ends are UPDATED to those of Nearest Neighbours
        #using the following algorith
        y_next[0]=2*(1-0.5*r**2)*y_current[0]-\
        y_previous[0]+r**2*(y_current[1])

        y_next[-1]=2*(1-0.5*r**2)*y_current[-1]-\
        y_previous[-1]+r**2*(y_current[-2])

        for i in range(n-1):
            y_next[i+1]=2*(1-r**2)*y_current[i+1]-\
            y_previous[i+1]+r**2*(y_current[i+2]+y_current[i])




        for i in range(n+1):
            #nearest neighbor algorithm (now for all n)
            y_previous[i]= y_current[i]
            y_current[i] = y_next[i]





        #creating a series of modulo operators and setting the remainder
        #eqaul to zero to plot the generated waves
        #at specified rates at specfied generations.
        if  (j%10 ==0 and 5<=j<=95):
            plt.plot(y_next[:])

        if  (j%50 ==0 and not 5<=j<=200 ):
            plt.plot(y_next[:])


    return np.vstack((y_previous,y_current,y_next))



#%%
def one_end_oscillate(amplitude,omega,dx,l):
    """
    Solution of wave equation for a string
    when one end if fixed and one end is free to oscillate.
    dx is the grid spacing parameter in meters, and l is length of string.
    Parameter for the wave speed is set to 300 m/s in script.
    Omega, Amplitude are part of the equation designated for the movement
    of the string element at the start (there is a fixed end)
    This equation is: y(i=0) = Amplitude*sin(omega*time)

    This is a vectorised version of the code provided.

    There are 3 vectors containing positional information for the system
    y_new, y_current and y_previous. The vectorised version serves as a guide
    to one--clearly understand the the algorithms--
    and two: provides a more effiecient way to to update
    the information.
    """
    #Define Constants
    c = 300    # wave speed in m/s
    dt = dx/c  # time in seconds
    r = c*dt/dx


    n = int(l/dx) # number of grid points on the string - 1
    #time value of interest
    if n>100:
        n=100

    #preallocate memory for speed
    y_current=np.zeros(n+1)
    y_previous=np.zeros(n+1)
    y_next=np.zeros(n+1)




    # Initial Condition (excluding the fixed end boundary)
    for i in range(n+1):
        y_current[i]=y_previous[i]= amplitude* np.sin(omega*(i)*dx)

    #Now specify Boudary conditions- only for end boundries-

    y_previous[-1]=0
    y_current[-1]=0
    y_next[-1]=0


    plt.figure()
    ax = plt.gca()
    ax.get_xaxis().set_ticks([])
    ax.set_xlabel("time (au)")
    ax.set_ylabel("displacement (au)")
    ax.set_title("Wave Motion Simulation on a String-With One Free Dnd\n\
    and One End set to Oscillate: Wave Displacement at Different Times",\
    family='monospace',size=12, weight='bold')


    for j in range(500):


        for i in range(0,n-1):
            y_next[i+1]=2*(1-r**2)*y_current[i+1]-\
            y_previous[i+1]+r**2*(y_current[i+2]+y_current[i])


        for i in range(n-1):
            #nearest neighbor algorithm (now for all n except fixed end boundary)
            y_previous[i+1]= y_current[i+1]
            y_current[i+1] = y_next[i+1]

        #creating a series of modulo operators and setting the remainder
        #eqaul to zero to plot the generated waves
        #at specified rates at specfied generations.
        if (j%50==0):
            plt.plot(y_next[:])

    ax.legend("",title='dx= %s and $\omega$= %s' %(dx,omega))
    return np.vstack((y_previous,y_current,y_next))







#%%$







y_one_end_oscillate=one_end_oscillate(amplitude=1,omega=2000,dx=0.01,l=1)
y_one_end_oscillate=one_end_oscillate(amplitude=1,omega=1950,dx=0.01,l=1)
y_one_end_oscillate=one_end_oscillate(amplitude=1,omega=1350,dx=0.01,l=1)
y_one_end_oscillate=one_end_oscillate(amplitude=1,omega=600,dx=0.01,l=1)

y_free=free_ends(dx=0.006,l=1)
y_free=free_ends(dx=0.017,l=1)
y_free=free_ends(dx=0.010,l=1)

y_fixed=fixed_ends(dx=0.01,l=1)
