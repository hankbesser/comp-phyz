#Molecular Dynamics

#### Henry Besser


#%% ALL comments on steps are in notebook
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pd.options.display.max_rows = 12

load_data = np.loadtxt("temperature_log.txt")

time_steps_data_set = pd.DataFrame(load_data, columns=\
                            ['Step Number [1 step = 2 fs]', 'Temperature [K]'])
time_steps_data_set

total_time_data_set = pd.DataFrame.from_items([('Time [fs}_____',\
            load_data[:,0]*2), ('Temperature [K]',load_data[:,1])])
total_time_data_set

x_to_fit = load_data[:,0]*2
y_to_fit = load_data[:,1]


from scipy.optimize import curve_fit

#The function and paremters previously descibed
def func(x, a, b, c, d):
    return a*np.exp(-b*d*x)+c

# curve fit function takes 4 values
#1. The exponential function
#2. x_to_fit is the time of simulation
#3. y_to_fit is the noisy data produced and in which we are trying to fit
#4. The initial guess of the 4 parameters in which the function of
# time depends on time

# The curve fit function returns two values (both in array form)
#1. p_est: Optimal values for the parameters
#          so that the sum of the squared error is minimized
#2. err_est: the covariance matrix of the estimates for the paramters,
#            The diagonals are the variances of the individual parameters.

p_est, err_est = curve_fit(func, x_to_fit, y_to_fit,[66.87,0.0146,200,0.095])

#%%
# Results:

# Plotting the optimal curve fit for the noisy average temperature data

plt.figure()
ax = plt.gca()

plt.plot(x_to_fit, y_to_fit,color='black', markersize=8, linestyle='-')
plt.plot(x_to_fit, func(x_to_fit, *p_est), color='magenta', linewidth=2)

ax.set_xlabel("Time [fs]")
ax.set_ylabel("Temperature [K]")

ax.set_title('Cooling of Ubiquitin: Temperature v. Time:\nTime Step = 2 fs',\
                                    family='monospace',size=10, weight='bold')

ax.legend(("Simulation Data", "Model Fit"), title= 'Average Temperature [K]:',\
                                            loc=1, fontsize=9)
plt.show()

#%%
# #### Printing parameter estimates
# #### The last value in the array p_est (parameter estimate) is the
# #### unscaled DIFFUSION Parameter.

print("Parameter Estimate: {0}".format(p_est))
#%%
# The amount of variation explained by the model ( given by the the diagonals of
# the covariance matrix) are minimal as all the parameters for the simulation --
# besides the thermal diffusivity parameter-- were provided.

print("Covariance Matrix: {0}".format(err_est))
