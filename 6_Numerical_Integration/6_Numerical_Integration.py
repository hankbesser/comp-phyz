# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:53:09 2016

@author: hbesser
"""

#%%
import matplotlib.pyplot as plt
import numpy as np
#%%

#Preface: if computing many arrays for each theta_max, you must NOT view 
#visualizations inline in Spyder because the legend will crowd the plot.
#So simply change graphics backend to Automatic in Preferences 

#Also this script could have been made without defining a function,
#and input the theta_max and thetha paremeters directly in the script.
#However it was an intriguing task to define a function that would not only 
#plot the Period vs theta_max, but also all 
#the theta*i values for each theta_max
#no matter how many input values are assigned to
#theta_max or what input is assigned to theta_step_size     

def period_numerical_integration(theta_max, theta_step_size):
    """
    Approximates the period a non-linear oscillator by numerical integration.
    Returns and Prints the Period ---PLUS return the the cumulated sum after 
    discretized theta to calculate the area under the curve in sequence.
    
    Input for theta_max must be an array of values as demonstrated in the lab.
    """
    
    #Fixed Constants throughout the Lab
    g = 9.8 # acceleration of gravity
    length = 1.0 #meter 
    
    # step size that is input (in radians)
    d_theta = float(theta_step_size) # step size (in radians)
    
    
    # number of steps
    # (i.e numerical solutions)
    #for all the input theta_max
    #remember even if only there is only one theta_max
    #it must be in a in a 1-dimensional np array
    N_d_theta_dumby = theta_max/d_theta 
    
    #Number of steps must be an integer (i.e round down to a int data-type)
    N_d_theta = N_d_theta_dumby.astype(int)
    
    # for consistenty each array will be an will the value of the argmax
    #for the largest array
    #this will become more clear as the script pursues    
    arg_max_value = N_d_theta[np.argmax(N_d_theta)]
    
    #initialize
    #variable to store incremental additions
    #this is an array grid (i.e two dimensional array)
    d_period = np.zeros((arg_max_value,len(theta_max)))
    
    
    #initialize
    #all though not required, an intriguing visualiztion is seeing
    #the cumilative sum for the period after each change in period computation.
    #This array-grid will (i.e two dimensional array) store these vales. 
    accumulate_integrations = np.zeros((arg_max_value,len(theta_max)))
    
    #initialize
    #one dimenstional array to store final period values 
    T2 = np.zeros(len(theta_max))
    
    #scalar computation provided in the lab- computed outside of loop
    #for efficiency
    scalar = np.sqrt((8*length)/g)
    
    for i in range(0,len(theta_max)):
        
                
        
        #INITIAL VALUE is always zero
        d_period[:N_d_theta[i],i] = np.arange(0,theta_max[i]-d_theta,d_theta) 
        
        d_period[N_d_theta[i]:,i] = np.nan
          
        for j in range(0,arg_max_value):
            if j < N_d_theta[i]:
                accumulate_integrations[j,i] = scalar * ((d_theta)\
                / (np.sqrt(np.cos(d_theta*(j))-np.cos(theta_max[i]))))
            
            #for consitency in step-size, fill all values past 
            #the number numerical solution 
            else: 
                accumulate_integrations[j,i] = np.nan 
                
             
    
    d_T = d_period       
    
    #accumulate (cumulative sum) values to numerically solve the integral
    # Stores the sum for the specified theta_max
    accumulate_integrations = np.add.accumulate(accumulate_integrations) 

    
    #Now get period
    for i in range(0,len(theta_max)):

        T2[i] = accumulate_integrations[N_d_theta[i]-1,i]
        
        print("Theta_max =",theta_max[i],"rad")
        print("And, Period of Pendulum = ", T2[i],"s","\n")

   
    return d_T, accumulate_integrations, T2,theta_max 
    
    
 #%%       
        
d_T, all_ints, T2,theta_max_values = period_numerical_integration(\
        theta_max=np.linspace(np.pi/30,59*np.pi/60,20), theta_step_size=0.001)


#%%

#visualize only the Period for each  cumulative sum of 
#after the numerical intregration each theta_max.
#that is cumulative sum of after the numerical intregration up the Number
#of Sequences to iterate - 1 
       
plt.plot(theta_max_values, T2,'m-o',label='$\\pi/30$ rad to $59\\pi/60$ rad ')
ax = plt.gca()
        
ax.set_title('Non-Linear Pendulum-for One Period: Period v. $\\theta_{max}$ ; \n\
$\\theta_{max}$ from $\\pi/30$ to $59\\pi/60$ and $\Delta\\theta$ = 0.001 rad',\
                     family='monospace',size=12, weight='bold')

ax.set_xlabel("$\\theta_{max}$ (rad)")
ax.set_ylabel("Period (s)")

    
ax.set_xlim(left=0,right=3.4)
ax.set_ylim(bottom=0, top=7.0)
    
ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)
        
        
ax.legend(fontsize=10, loc= 2,title='20 $\\theta_{max}$ values from:')

plt.figure()
plt.show()        
        
        
#%%


#visualize ethe cumulative sum of after the numerical integration for
#each theta_max.
#the last point for each theta_max
#represents the period that was previously graphed.

marker_color =     ['m.', 'y.', 'k.', 'c.','b.', 'm.', 'y.', 'k.', 'c.','b.',\
                    'm.', 'y.', 'k.', 'c.','b.', 'm.', 'y.', 'k.', 'c.','b.',\
                    'm.', 'y.', 'k.', 'c.','b.', 'm.', 'y.', 'k.', 'c.','b.',\
                    'm.', 'y.', 'k.', 'c.','b.', 'm.', 'y.', 'k.', 'c.','b.',\
                    'm.', 'y.', 'k.', 'c.','b.', 'm.', 'y.', 'k.', 'c.','b.'] 
    
for i in range(0,len(T2)):
    plt.plot(d_T[:,i], all_ints[:,i],marker_color[i],markersize=4)
    ax = plt.gca()
        
    ax.set_title('Non-Linear Pendulum- One Period: Period v. $\\theta$ ; \n\
    $\\theta_{max}$ from $\\pi/30$ to $59\\pi/60$ and $\Delta\\theta$ = 0.001 rad',\
                     family='monospace',size=12, weight='bold')

    ax.set_xlabel("$\\theta$ (rad)")
    ax.set_ylabel("time (s)")

    ax.set_xlim(left=0,right=3.4)
    
    
    ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
    ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)
        
        
    ax.legend(theta_max_values,fontsize=10, loc= 2,title="$\\theta_{max}$ in rad")
        
       
        
plt.show()
    
