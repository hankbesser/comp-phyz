# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:39:51 2016

@author: hbesser
"""

#%%
import matplotlib.pyplot as plt
import numpy as np
#%%
def pendulum_euler_cromer(theta0, omega0, length, time0, time_f, dt):
    """
    Numerical solutions to the simple ossilatory motion problem.
    
    Calculates theta as a function of time using the Euler-Cromer method.
    
    This leads one to investigate the relationship between
    the amplitude and period of the oscillation.
    """
    

    g = 9.8 # acceleration of gravity
    
    dt = float(dt)  # time step (in seconds)
    
    N_dt = int((time_f-time0)/dt)   # number of time steps
                                    # (i.e numerical solutions)
    
    time_max = N_dt*dt # Total time (in seconds)
    
    time = np.linspace(time0, time_max, N_dt+1) # total time with 
                                                # N_dt number of time steps
    
    theta=np.zeros(time.size) # zero array
    omega=np.zeros(time.size) # zero array
    
    theta[0]= theta0 #initial condition
    omega[0]= omega0 #initial condition
    
    for i in range(0, N_dt): 
        
       # computing theta and omega with the Euler-Cromer method
       # NOTE: omega[i] is NOT used as in the euler method  
       
       # AND: omega[i+1] used to calculate  
       # the new value, theta[i+1] 
       
       # where the two first-order differential equations are; 
       # domega = -(g/length)*np.sin(theta[i]) AND
       # dtheta = omega[i+1]
        
        omega[i+1] = omega[i] - (g/length)*np.sin(theta[i])*dt 
        theta[i+1] = theta[i] + omega[i+1]*dt  
          
       
    return time, theta
    

#%%

#%%

# Now modifying script to calculate energy at each step time step
# to see if energy is conserved.

# We were not given the mass (or lack there of) of the pendulum.
# Therefore, the mass is made up and will designate mass as 1.
#This means theres is no need to put mass 
#in the equation ((...)*1--the mass-- will be the same number)



def pendulum_and_energy_euler_cromer(theta0,omega0,length,time0,time_f,dt):
    """
    Numerical solutions to energy of the system in 
    the ossilatory motion problem.
    
    Calculates energy as a function of time when the the Euler-Cromer method
    is implemented.
    
    This leads one to investigate if energy is conserved.
    """
    

    g = 9.8 # acceleration of gravity
    
    dt = float(dt)  # time step (in seconds)
    
    N_dt = int((time_f-time0)/dt)   # number of time steps
                                    # (i.e numerical solutions)
    
    time_max = N_dt*dt # Total time (in seconds)
    
    time = np.linspace(time0, time_max, N_dt+1) # total time with 
                                                # N_dt number of time steps
    
    theta=np.zeros(time.size) # zero array
    omega=np.zeros(time.size) # zero array
    energy = np.zeros(time.size) # zero array    
    
    
    theta[0]= theta0 #initial condition
    omega[0]= omega0 #initial condition
        
    
    
    
    for i in range(0, N_dt): 
        
       # computing theta and omega with the Euler-Cromer method
       # NOTE: omega[i] is NOT used as in the euler method  
       
       # AND: omega[i+1] used to calculate  
       # the new value, theta[i+1] 
       # where; 
       # domega = -(g/length)*np.sin(theta[i]) AND
       # dtheta = omega[i+1]
        
        omega[i+1] = omega[i] - (g/length)*np.sin(theta[i])*dt 
        theta[i+1] = theta[i] + omega[i+1]*dt  
    

    #as the omega and theta are arrays with a sequence of numbers  
    #at each time step and an initial condition, to calculate total energy
    #simply plug thetha and omega in the total energy equation      
    energy = 0.5 * (length)**2 * (omega)**2 + g*length*(1-np.cos(theta)) 
    
    return time, energy



#%%

#investigate the relationship between and 
#the amplitude and period of the oscillation

# define parameters: theta0, omega0, length, time0, time_f, dt

#theta0 = np.pi/12
time, theta1 = pendulum_euler_cromer(np.pi/12,0,1,0,10,0.004)

#theta0 = np.pi/6  
time, theta2 = pendulum_euler_cromer(np.pi/6,0,1,0,10,0.004)

#theta0 = np.pi/3
time, theta3 = pendulum_euler_cromer(np.pi/3,0,1,0,10,0.004)



    
    
#%%
# define parameters: theta0, omega0, length, mass, time0, time_f, dt

#By substituting the omega and theta arrays found at each time step 
#into the total energy expression, 
#when using the Euler-Cromer method energy osillates over over a cycle and 
#give (approximatley) a zero total contribution. i.e Total Energy 
#IS conserved. 


#Therefore, the Total Energy does NOT monotonically increases in time 
#like when the system is solved using the Euler method.  


#theta0 = np.pi/12
time, energy1 = pendulum_and_energy_euler_cromer(np.pi/12, 0, 1, 0, 10, 0.004)

#theta0 = np.pi/6
time, energy2 = pendulum_and_energy_euler_cromer(np.pi/6, 0, 1, 0, 10, 0.004)

#theta0 = np.pi/3
time, energy3 = pendulum_and_energy_euler_cromer(np.pi/3, 0, 1, 0, 10, 0.004)

#%%

#plotting all 3 figures:

#%%

#figure 1
#plot theta as a function of time 

plt.figure()
plt.plot(time, theta1, 'b', time, theta2,'r', time, theta3, 'g')
ax = plt.gca()

ax.set_title("Simple Pendulum: Euler-Cromer Method\n\
Length = 1m and Time Step = 0.004 s ",\
family='monospace',size=14, weight='bold')

ax.set_xlabel("time (s)")
ax.set_ylabel("$\\theta$ (radians)")

ax.set_ylim(bottom=-1.2, top=1.2)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$\\theta_{0} = \pi/12$","$\\theta_{0} = \pi/6$",\
"$\\theta_{0} = \pi/3$",),fontsize=12, loc= 4)

plt.show()



#%%

#figure 2
#plot enrgy as a function of time 


plt.figure()
plt.plot( time,energy1, 'b', time,energy2, 'r', time,energy3, 'g')
ax = plt.gca()

ax.set_title("Total Energy Conserved: the Euler-Cromer Method\n\
Length = 1m, Mass = 1 kg, Time Step = 0.004 s ",\
family='monospace',size=14, weight='bold')

ax.set_xlabel("time (s)")
ax.set_ylabel("energy (J)")

ax.set_ylim(bottom=0, top=5.5)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("Total Energy when $\\theta_{0} = \pi/12$",\
"Total Energy when $\\theta_{0} = \pi/6$",\
"Total Energy when $\\theta_{0} = \pi/3$",),fontsize=12, loc= 5)

plt.show()



#%%

#find period of ossilation for all 
#three different initial displacement values 
#very simple by the way that the functions were written
dt=0.004 
print(np.argmin(theta1[0:int(1.8/dt)]))
print(np.argmin(theta2[0:int(1.8/dt)]))
print(np.argmin(theta3[0:int(1.8/dt)]))

#0:argmin * 2, to get time representing full period index, 
#but need to include the last index so +2


T1 = theta1[0:251*2+2]
time_theta1 = time[0:251*2+2]
print(time_theta1[-1]) # period, T, of oscillation 

T2 = theta2[0:255*2+2]
time_theta2 = time[0:255*2+2]
print(time_theta2[-1]) # period, T, of oscillation

                          
T3 = theta3[0:269*2+2]
time_theta3 = time[0:269*2+2]
print(time_theta3[-1]) # period, T, of oscillation

#%%

#figure 3
#plot theta as a function of time for a period of ossilation 

plt.figure()
plt.plot(time_theta1, T1, 'b', time_theta2, T2, 'r', time_theta3, T3, 'g')
ax = plt.gca()

ax.set_title("Simple Pendulum-One Period: Euler-Cromer Method\n\
Length = 1m and Time Step = 0.004 s ",\
family='monospace',size=14, weight='bold')

ax.set_xlabel("time (s)")
ax.set_ylabel("$\\theta$ (radians)")

ax.set_xlim(left=0, right=2.5)
ax.set_ylim(bottom=-2.5, top=2.5)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$\\theta_{0} = \pi/12$","$\\theta_{0} =\
\pi/6$","$\\theta_{0} = \pi/3$",),fontsize=12, loc= 4)

plt.show()
