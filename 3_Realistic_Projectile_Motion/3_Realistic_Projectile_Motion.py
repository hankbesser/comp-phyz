# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 18:10:41 2016

@author: Hank Besser
"""

import matplotlib.pyplot as plt
import numpy as np

#%%

def baseball_no_wind(v, x0, y0, theta, time0, time_f, dt):
    """
    Calculates solution to the baseball trajectory problem using 
    the Euler method, including the 
    velocity dependence of the drag force but no wind effect. 
    """
    g = 9.8 
    
    dt = float(dt)  # time step (in seconds)
    
    N_dt = int((time_f-time0)/dt)   # number of time steps
                                    # (i.e numerical solutions)
    
    time_max = N_dt*dt # Total time (in seconds)
    
    time = np.linspace(time0, time_max, N_dt+1) # total time with 
                                            # N_dt number of time steps
    x=np.zeros(time.size) # zero array 
    y=np.zeros(time.size) # zero array 
    vel_x=np.zeros(time.size) # zero array 
    vel_y=np.zeros(time.size) # zero array 
    vel_x[0]=v*np.cos(np.radians(theta)) #initial condition  
    vel_y[0]=v*np.sin(np.radians(theta)) #initial condition
    x[0]=x0 #initial condition
    y[0]=y0 #initial condition
    
    for i in range(0, N_dt): 
    
        velocity = np.sqrt(vel_x[i]**2 + vel_y[i]**2)
        
        #B2/m - drag coefficent- air resistance
        drag_co = 0.0039 + (0.0058/(1+ np.exp((velocity-35)/5)))            
        
        #euler method 
        vel_x[i+1] = vel_x[i] - drag_co * velocity * vel_x[i] *  dt
        
        #euler method
        vel_y[i+1] = vel_y[i] - g*dt - drag_co * velocity * vel_y[i] *  dt
        
        #euler method
        x[i+1] = x[i] + vel_x[i] *dt 
        
        #euler method
        y[i+1] = y[i] + vel_y[i] *dt
        
    return x,y
#%%

def baseball_wind(v, v_wind, x0, y0, theta, time0, time_f, dt):
    """
    Calculates solution to the baseball trajectory problem using 
    the Euler method, including the 
    velocity dependence of the drag force and the effect of wind. 
    """
    g = 9.8 
    
    dt = float(dt)  # time step (in seconds)
    
    N_dt = int((time_f-time0)/dt)   # number of time steps
                                    # (i.e numerical solutions)
    
    time_max = N_dt*dt # Total time (in seconds)
    
    time = np.linspace(time0, time_max, N_dt+1) # total time with 
                                            # N_dt number of time steps
    x=np.zeros(time.size) # zero array
    y=np.zeros(time.size) # zero array
    vel_x=np.zeros(time.size) # zero array
    vel_y=np.zeros(time.size) # zero array
    vel_x[0]=v*np.cos(np.radians(theta)) #initial condition 
    vel_y[0]=v*np.sin(np.radians(theta)) #initial condition
    x[0]=x0 #initial condition
    y[0]=y0 #initial condition
    
       
    
    for i in range(0, N_dt):
          
        velocity = np.sqrt(vel_x[i]**2 + vel_y[i]**2)
        
        #B2/m - drag coefficent- air resistance  
        drag_co = 0.0039 + (0.0058/(1+ np.exp((velocity-35)/5)))            
        
        # adding effects of wind
        
        #euler method
        vel_x[i+1] = vel_x[i] - drag_co * np.abs(velocity - v_wind) *\
                                                    ((vel_x[i])-v_wind) *  dt
        #euler method        
        vel_y[i+1] = vel_y[i] - g*dt - drag_co * np.abs(velocity - v_wind) *\
                                                            (vel_y[i]) *  dt
        
        
        #euler method       
        x[i+1] = x[i] + vel_x[i] *dt 
        
        #euler method
        y[i+1] = y[i] + vel_y[i] *dt
        
    return x,y
#%%

# define parameters: v, x0, y0, theta, time0, time_f, dt
#no wind
x1, y1 = baseball_no_wind(50, 0, 0, 35, 0, 5, 0.001)

# define parameters: v, v_wind, x0, y0, theta, time0, time_f, dt
#tailwind
x1_w1, y1_w1 =  baseball_wind(50,  4, 0, 0, 35, 0, 6, 0.001)

# define parameters: v, v_wind, x0, y0, theta, time0, time_f, dt
#headwind
x1_w2, y1_w2 =  baseball_wind(50,  -4, 0, 0, 35, 0, 5, 0.001)

#%%        

#plot trajectories until ball hits ground (i.e for y>=0)
plt.figure()
plt.plot(x1,y1,x1_w1,y1_w1,x1_w2,y1_w2)
ax = plt.gca()

ax.set_title("Trajectory of a Baseball",\
family='monospace',size=14, weight='bold')

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

ax.set_ylim(bottom=0)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("no wind effects", "v_wind > 0 (tailwind)",\
                    "v_wind < 0 (headwind)"),fontsize=12)
plt.show()



#%%

def baseball_spin(v, x0, y0, z0, theta, omega, time0, time_f, dt):
    """
    Calculates solution to the baseball trajectory problem using 
    the Euler method, including the effects of spin 
    """
    g = 9.8 
    
    dt = float(dt)  # time step (in seconds)
    
    N_dt = int((time_f-time0)/dt)   # number of time steps
                                    # (i.e numerical solutions)
    
    time_max = N_dt*dt # Total time (in seconds)
    
    time = np.linspace(time0, time_max, N_dt+1) # total time with 
                                            # N_dt number of time steps
    x=np.zeros(time.size)
    y=np.zeros(time.size)
    z=np.zeros(time.size)
    vel_x=np.zeros(time.size)
    vel_y=np.zeros(time.size)
    vel_z=np.zeros(time.size)
    vel_x[0]=v*np.cos(np.radians(theta))
    vel_y[0]=v*np.sin(np.radians(theta))
    vel_z[0]=0      
    x[0]=x0
    y[0]=y0
    z[0]=z0
       
    for i in range(0, N_dt): 
    
        velocity = np.sqrt(vel_x[i]**2 + vel_y[i]**2)
        
        #B2/m - drag coefficent- air resistance     
        drag_co = 0.0039 + (0.0058/(1+ np.exp((velocity-35)/5)))            
        
        #s0/m - spin-coefficent- effects of spin
        s0_co = 4.1e-4 # m = 149 g
         
        vel_x[i+1] = vel_x[i] - drag_co * velocity * vel_x[i] *  dt
        vel_y[i+1] = vel_y[i] - g*dt 
        
        # Important: Omega is parrallel to y-axis         
        vel_z[i+1] = vel_z[i] - s0_co * -1*(omega) * vel_x[i] * dt   
        
               
        x[i+1] = x[i] + vel_x[i] *dt 
        y[i+1] = y[i] + vel_y[i] *dt
        z[i+1] = z[i] + vel_z[i] *dt 
    return x,y,z
#%%
# define parameters: v, x0, y0, z0, theta, omega, time0, time_f, dt
x_s, y_s, z_s = baseball_spin(30, 0, 50, 0, 0, 30, 0, 4, 0.01)
#%%
# plotting y as function of x
plt.figure()

plt.plot(x_s, y_s)
ax = plt.gca()

ax.set_title("Trajectory of a Baseball: Effects of Spin-\n\
y as a Function of x",\
family='monospace',size=12, weight='bold')

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

ax.set_ylim(bottom=0)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(('vertical deflection (y)',),fontsize=12)

plt.show()
#%%
# plotting z as function of x
plt.figure()

plt.plot(x_s, z_s)
ax = plt.gca()

ax.set_title("Trajectory of a Baseball: Effects of Spin-\n\
z as a Function of x",\
family='monospace',size=12, weight='bold')

ax.set_xlabel("x (m)")
ax.set_ylabel("z (m)")

ax.set_ylim(bottom=0)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("horizontal deflection (z)",),fontsize=12, loc=2)

plt.show()


#%%
# Both on same plot
plt.figure()

plt.plot(x_s, y_s, x_s, z_s)
ax = plt.gca()

ax.set_title("Trajectory of a Baseball: Effects of Spin",\
family='monospace',size=12, weight='bold')

ax.set_xlabel("x(m)")
ax.set_ylabel("y(m) or z(m)")

ax.set_ylim(bottom=0)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("vertical deflection (y)", "horizontal deflection (z)",))

plt.show()