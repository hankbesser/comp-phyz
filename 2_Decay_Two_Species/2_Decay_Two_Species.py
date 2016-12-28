# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:43:01 2016

@author: hbesser
"""

import numpy as np
import matplotlib.pyplot as plt

#%% 
def euler_decay_two_species(start_A, start_B, tau_A, tau_B, time_max, dt):
    """
    Calculates solution to the radioactive decay problem using 
    the Euler method. 
    """
    dt = float(dt)  # time step (in seconds)
    
    N_dt = int(round(time_max/dt))  # number of time steps
                                    # (i.e numerical solutions)
    
    time_max = N_dt*dt # Total time (in seconds)
    
    time = np.linspace(0, time_max, N_dt+1) # total time with 
                                            # N_dt number of time steps
    
    N_A = np.zeros(time.shape)              # zero array of nuc[i] values 
    N_B = np.zeros(time.shape)                                        
      

    N_A[0] = start_A    # assigns initial number of nuclei 
    N_B[0] = start_B    # as the initial conditon
                        # (i.e. for nuc[i], when i=0)
    
    for i in range(0, N_dt):                   # i=0,1,...,N_dt-1
        N_A[i+1] = N_A[i] - (N_A[i]/tau_A)*dt  # Euler method
        N_B[i+1] = N_B[i] - (N_B[i]/tau_B)*dt + (N_A[i]/tau_A)*dt          
    return time, N_A, N_B     
     

#%%

time1, NA1, NB1 = euler_decay_two_species(start_A=100, start_B=100,\
                                    tau_A=1, tau_B=3,time_max=20, dt=0.01)
plt.figure()

plt.plot(time1, NA1, 'r.',time1, NB1,'m+') 

ax = plt.gca()

ax.set_title("Radioactive Decay when $tau_{A}$/$tau_{B}$ < 1;\n\
$N0_{A}$=100, $N0_{B}$=100, $tau_{A}$=1, $tau_{B}$=3, $dt$=0.01",\
family='monospace',size=16, weight='bold')

ax.set_xlabel("Time [seconds]")
ax.set_ylabel("Number of Nuclei")

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$N_{A}$", "$N_{B}$"),fontsize=16)


#%%
#When tau_A < tau_B (i.e when tau_A \ tau_B is smaller than 1)
time1, NA1, NB1 = euler_decay_two_species(start_A=100, start_B=100,\
                                    tau_A=1, tau_B=20,time_max=20, dt=0.01)
plt.figure()

plt.plot(time1, NA1, 'r.',time1, NB1,'m+') 

ax = plt.gca()

ax.set_title("Radioactive Decay when $tau_{A}$/$tau_{B}$ < 1;\n\
$N0_{A}$=100, $N0_{B}$=100, $tau_{A}$=1, $tau_{B}$=20, $dt$=0.01",\
family='monospace',size=16, weight='bold')

ax.set_xlabel("Time [seconds]")
ax.set_ylabel("Number of Nuclei")

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$N_{A}$", "$N_{B}$"),fontsize=16)



#%%
#When tau_A >>> tau_B (i.e when tau_A \ tau_B is very large)
time2, NA2, NB2 = euler_decay_two_species(start_A=100, start_B=100,\
                                    tau_A=20, tau_B=1,time_max=20, dt=0.01)
plt.figure()

plt.plot(time2, NA2, 'r.',time1, NB2,'m+') 

ax = plt.gca()

ax.set_title("Radioactive Decay when $tau_{A}$/$tau_{B}$ is very large;\n\
$N0_{A}$=100, $N0_{B}$=100, $tau_{A}$=20, $tau_{B}$=1, $dt$=0.01",\
family='monospace',size=16, weight='bold')

ax.set_xlabel("Time [seconds]")
ax.set_ylabel("Number of Nuclei")

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$N_{A}$", "$N_{B}$"),fontsize=16)


#%%
#When tau_A = tau_B (i.e when tau_A \ tau_B is 1)
time2, NA2, NB2 = euler_decay_two_species(start_A=100, start_B=100,\
                                    tau_A=3, tau_B=3,time_max=20, dt=0.01)
plt.figure()

plt.plot(time2, NA2, 'r.',time1, NB2,'m+') 

ax = plt.gca()

ax.set_title("Radioactive Decay when $tau_{A}$/$tau_{B}$ = 1;\n\
$N0_{A}$=100, $N0_{B}$=100, $tau_{A}$=50, $tau_{B}$=1, $dt$=0.01",\
family='monospace',size=16, weight='bold')

ax.set_xlabel("Time [seconds]")
ax.set_ylabel("Number of Nuclei")

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$N_{A}$", "$N_{B}$"),fontsize=16)



#%%
time, NA, NB = euler_decay_two_species(start_A=100, start_B=100,\
                                       tau_A=1, tau_B=3,time_max=20, dt=0.01)   
tau_A = 1 
tau_B = 3

#Analytical solutions
analytical_NA = NA[0]*np.exp(-time/tau_A)
analytical_NB =  NB[0]*np.exp(-time/tau_B) +\
(NA[0]/((tau_A/tau_B)-1))*(np.exp(-time/(tau_A))-(np.exp(-time/(tau_B))))   
 
plt.figure()

plt.plot(time, NA, "r.",linewidth=1) 
plt.plot(time, NB,"m+", linewidth=1)
plt.plot(time, analytical_NA, "k-",linewidth=2 )
plt.plot(time, analytical_NB, "b-",linewidth=2 )


ax = plt.gca()

ax.set_title("Radioactive Decay: Numerical Solutions and Analytical Solutions\n\
$N0_{A}$=100, $N0_{B}$=100,$tau_{A}$=1, $tau_{B}$=3, $dt$=0.01",\
family='monospace',size=14, weight='bold')

ax.set_xlabel("Time [seconds]")
ax.set_ylabel("Number of Nuclei")

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("Numerical $N_{A}$", "Numerical $N_{B}$", "Analytical $N_{A}$",\
"Analytical $N_{B}$"  ),fontsize=13)

 




#%% 
time, NA, NB = euler_decay_two_species(start_A=100, start_B=100,\
                                       tau_A=1, tau_B=3,time_max=20, dt=0.1)   
tau_A = 1 
tau_B = 3

#Analytical solutions
analytical_NA = NA[0]*np.exp(-time/tau_A)
analytical_NB =  NB[0]*np.exp(-time/tau_B) +\
(NA[0]/((tau_A/tau_B)-1))*(np.exp(-time/(tau_A))-(np.exp(-time/(tau_B))))   
 
plt.figure()

plt.plot(time, NA, "r.",linewidth=1) 
plt.plot(time, NB,"m+", linewidth=1)
plt.plot(time, analytical_NA, "k-",linewidth=2 )
plt.plot(time, analytical_NB, "b-",linewidth=2 )


ax = plt.gca()

ax.set_title("Radioactive Decay: Numerical Solutions and Analytical Solutions\n\
$N0_{A}$=100, $N0_{B}$=100,$tau_{A}$=1, $tau_{B}$=3, $dt$=0.1",\
family='monospace',size=14, weight='bold')

ax.set_xlabel("Time [seconds]")
ax.set_ylabel("Number of Nuclei")

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("Numerical $N_{A}$", "Numerical $N_{B}$", "Analytical $N_{A}$",\
"Analytical $N_{B}$"  ),fontsize=13)

  

#%%
def calc_runge(start_atoms, tau, time_max, dt):
    """
    Calculates solution to the radioactive decay problem using 
    the 2nd order Runge-Kutta method. 
    """
    dt = float(dt)                        # time step (in seconds)
    
    N_dt = int(round(time_max/dt))        # number of time steps (i.e numerical solutions)
    
    time_max = N_dt*dt                    # Total time (in seconds)
    
    
    time_r = np.linspace(0, time_max, N_dt+1)  # total time with N_dt number of time steps
    
    nuc = np.zeros(time_r.size)                # zero array nuc[i] values (number of time steps)  
      

    nuc[0] = start_atoms    # assigns initial number of nuclei
                            # as the initial conditon (i.e. nuc[i], when i=0)
    
    for i in range(0, N_dt):                   # i=0,1,...,N_dt-1
        dx = -nuc[i]/tau
        nuc_m = nuc[i] +0.5*dt*dx
        dx2 = -nuc_m/tau
        nuc[i+1] = nuc[i]+dt*dx2  #  2nd order Runge-Kutta method
    return time_r, nuc

#%%
time_r, nuc_r = calc_runge(start_atoms=100, tau=1, time_max=20, dt=0.01)

time, NA, NB = euler_decay_two_species(start_A=100, start_B=100,\
                                       tau_A=1, tau_B=3,time_max=20, dt=0.1)  

plt.figure()

plt.plot(time, NA, "b.",markersize=3) 
plt.plot(time_r, nuc_r,"m+", markersize=7)

plt.plot(time_r, nuc_r, 'b.',time, NA,'g+') 

ax = plt.gca()

ax.set_title("Radioactive Decay: Comparing Euler\n and 2nd Order Runge-Kutta\
 for type N_A\n\
$N0_{A}$=100,$tau_{A}$=1, $dt$=0.01",\
family='monospace',size=14, weight='bold')

ax.set_xlabel("Time [seconds]")
ax.set_ylabel("Number of Nuclei")

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("Euler", "2nd order Runge-Kutta"),fontsize=10)

plt.show()    