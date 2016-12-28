# Henry (Hank) Besser

#%%
import numpy as np
import matplotlib.pyplot as plt

#%% Figure 1
time = np.linspace(0,100,101)


A = np.array([1000.0,4000.0,9000.0,5000.0])
B = np.array([0.0,10.0,20.0,40.0])

alpha = np.array([0.01, 0.03,0.04,0.06])
beta = np.array([100000000.0,200000000.0,100000.0,8000000.0])


viral_load = np.zeros((len(A),len(time)))


for i in np.arange(0,len(A)):
    # sequence for storing the values in viral_load[i] matricies 
    viral_load[i] = A[i] * np.exp(-alpha[i]*time)+B[i]*np.exp(-beta[i]*time)


plt.figure()
plt.plot(time,viral_load[0])
plt.plot(time,viral_load[1])
plt.plot(time,viral_load[2])
plt.plot(time,viral_load[3])


#%% Figure 2

HIV_data_set = np.load("HIVseries.npz")

time = HIV_data_set['time_in_days']

concentration = HIV_data_set['viral_load']


plt.figure()

plt.plot(time, concentration, 'r.', label="Viral Load Data")       
plt.legend()

ax = plt.gca()

ax.set_title("Plotting the Data for Viral Load\nin a HIV-Positive Patient's\
Blood\n",family='monospace', size=14, weight='bold')

ax.set_xlabel("Time since Administration of Treatment [Days]")
ax.set_ylabel("Virus Concentration in Blood [au]")

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)


#%% Figure 3
time_fit = np.linspace(0,10,101) 
A = 170000
B = 1000

alpha = 0.5 #T-Cell Infection Rate       
beta = 0.7  

viral_load = A * np.exp(-alpha*time_fit) + B * np.exp(-beta*time_fit)


plt.figure()

plt.plot(time, concentration, 'r.', time_fit, viral_load, 'b-')      

ax = plt.gca()

ax.set_title("Fitting the Plotted Data for the\nViral Load of a HIV-Positive\
Patient's Blood\n",family='monospace', size=14, weight='bold')

ax.set_xlabel("Time since Administration of Treatment [Days]")
ax.set_ylabel("Virus Concentration in Blood [au]")

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("Viral Load Data", "Model Fit"))

plt.show()
