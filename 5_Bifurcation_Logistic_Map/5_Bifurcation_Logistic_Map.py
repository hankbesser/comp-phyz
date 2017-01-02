"""
Created on Sat Oct 22 11:43:57 2016

@author: hbesser
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
#%%

def logistic_map(x_0,n_0, n_f, mu):
    """
    General behavior of a logistic map.

    Used for visualizing x_n vs. n for a certain value of mu,
    in range n_0 to n_f, and starting with x0

    Model is defined by relation-- x_(n+1) = mu*x_n*(1-x_n)
    """

    # total time with with n_f-n_0 generations (i.e steps)
    n_array = np.linspace(n_0, n_f, int(n_f-n_0)+1)

    x_array = np.zeros(n_array.size) #zero array
    x_array[0]= x_0  # initial x

    for i in range(0, int(n_f-n_0)):
        x_array[i+1] = mu * x_array[i] * (1.0 - x_array[i])

    return n_array, x_array  #gathering data that is needed


#%%
def iteration(x_0,n_0, n_f, mu):
    """
    Fill an array with an iteration of steady state (n>>1) x_n values
    as a function of mu at a specified mu value. The individual iterations
    are represented by vertical slices.

    Used for visualzing x_n vs. mu for a
    certain value of mu, in range n_0 to n_f, and starting with x0

    This function is called by the bifurcation_diagram to iterate

    Model is defined by relation x_(n+1) = mu*x_n*(1-x_n)

    """
    # total time with with n_f-n_0 generations (i.e steps)
    n_array = np.linspace(n_0, n_f, int(n_f-n_0)+1)

    x_array = np.zeros(n_array.size) #zero array
    x_array[0]= x_0  # initial x

    mu_array= np.zeros(n_array.size) #zero array
    mu_array= mu_array+mu #all elements in mu_array set to value of mu


    for i in range(0, int(n_f-n_0)):
        x_array[i+1] = mu * x_array[i] * (1.0 - x_array[i])

    return mu_array, x_array #gathering data that is needed


#%%
def bifurcation_diagram(x_0,n_0,n_f,step_size):
    """
    Plot the iterated logistic map for all the mu values from 1..4
    with an iteration range of n_0 to n_f and step value of step_size
    """

    for i in np.arange(1,4,step_size):

        # get the array of iterations from iteration function
        mu_array, x_array = iteration(x_0=x_0,n_0=n_0, n_f=n_f,mu=i)

        # decrease size of points for creating the plot
        plt.plot(mu_array[300:-1],x_array[300:-1],'r.',markersize=1)

#%%
                    # Paremeters
n_array1, x_array1 = logistic_map(0.3,0, 100, 2.0)
n_array2, x_array2 = logistic_map(0.3,0, 100, 3.1)
n_array3, x_array3 = logistic_map(0.3,0, 100, 3.5)
n_array3_8, x_array3_8 = logistic_map(x_0=0.3,n_0=0, n_f=100, mu=3.8)
#%%
                    # Paremeters
mu_array1, x_array4 = iteration(x_0=0.3,n_0=0, n_f=400, mu=3.5)
mu_array2, x_array5 = iteration(x_0=0.3,n_0=0, n_f=400, mu=3.6)
mu_array3, x_array6 = iteration(x_0=0.3,n_0=0, n_f=400, mu=3.7)

#%%

#Visualizations

#%%%
#Part 1, x_n vs. n: when mu = 2.0

plt.figure()

plt.plot(n_array1, x_array1,"r.-")
ax = plt.gca()

ax.set_title('Logistic Map $x_{n}$ vs. $n$: where $\mu$ = 2.0',\
family='monospace',size=14, weight='bold')

ax.set_xlabel('n [au]',fontsize =14)
ax.set_ylabel('$x_{n}$ [au]',fontsize =14)

ax.set_ylim(bottom=0, top=1.05)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$\mu = 2.0$",),fontsize=12, loc= 4)

plt.show()
#%%

#Part 1, x_n vs. n: when mu = 3.1
plt.figure()


plt.plot(n_array2, x_array2,"b.-")
ax = plt.gca()

ax.set_title('Logistic Map $x_{n}$ vs. $n$: where $\mu$ = 3.1',\
family='monospace',size=14, weight='bold')

ax.set_xlabel('n [au]',fontsize =14)
ax.set_ylabel('$x_{n}$ [au]',fontsize =14)

ax.set_ylim(bottom=0, top=1.05)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$\mu = 3.1$",),fontsize=12, loc= 4)

plt.show()

#%%

#Part 1, x_n vs. n: when mu = 3.5

plt.figure()


plt.plot(n_array3, x_array3,"g.-")
ax = plt.gca()

ax.set_title('Logistic Map $x_{n}$ vs. $n$: where $\mu$ = 3.5',\
family='monospace',size=14, weight='bold')

ax.set_xlabel('n [au]',fontsize =14)
ax.set_ylabel('$x_{n}$ [au]',fontsize =14)

ax.set_ylim(bottom=0, top=1.05)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$\mu = 3.5$",),fontsize=12, loc= 4)

plt.show()

#%%

#Part 1, x_n vs. n: when mu = 2.0, 3.1, 3.5, and 3.8 in same plot
plt.figure()

plt.plot(n_array1, x_array1,"r.-",n_array2,\
         x_array2,"b.-",n_array3, x_array3,"g.-",n_array3_8, x_array3_8,"c.-")
ax = plt.gca()

ax.set_title("Logistic Map $x_{n}$ vs. $n$:\n\
All Three Sets in Same Plot-- Alongside Chaotic Behavior",\
family='monospace',size=14, weight='bold')

ax.set_xlabel('n [au]',fontsize =14)
ax.set_ylabel('$x_{n}$ [au]',fontsize =14)

ax.set_ylim(bottom=0, top=1.05)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$\mu = 2.0$","$\mu = 3.1$","$\mu = 3.5$","$\mu = 3.8$",),\
fontsize=12, loc= 4)

plt.show()

#%%

#Part 2,  plotting steady state vaules to obtain
#bifurcation diagram:
#visualzing x_n vs. mu when mu = 3.5, 3.6, and 3.7

plt.figure()

plt.plot(mu_array1[300:-1], x_array4[300:-1],'k.', markersize=2)
plt.plot(mu_array2[300:-1], x_array5[300:-1],'m.', markersize=2)
plt.plot(mu_array3[300:-1], x_array6[300:-1],'c.', markersize=2)
ax = plt.gca()

ax.set_title("Logistic Map: Steady State Values\n$x_{n}$ vs. $\mu$: where \
$\mu$ = 3.5 and $\mu$ = 3.6, and  $\mu$ = 3.7",\
family='monospace',size=14, weight='bold')

ax.set_xlabel('$\mu$ [au]',fontsize =14)
ax.set_ylabel('$x_{n}$ [au]',fontsize =14)

ax.set_ylim(bottom=0, top=1.05)
ax.set_xlim(left=0, right=4.00)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

ax.legend(("$\mu = 3.5$","$\mu = 3.6$","$\mu = 3.7$",),fontsize=12, loc= 2)

plt.show()

#%%

#Part 3, extending the plot to cover
# mu = 1....4 with step size of 0.0005
plt.figure()

ax = plt.gca()

ax.set_title("Bifurcation Diagram $x_{n}$ vs. $\mu$:\n\
where $\mu$ = 1 to 4 and Step Size = 0.05",\
family='monospace',size=14, weight='bold')

ax.set_xlabel('$\mu$ [au]',fontsize =14)
ax.set_ylabel('$x_{n}$ [au]',fontsize =14)

ax.set_ylim(bottom=0, top=1.05)
ax.set_xlim(left=1.0, right=4.00)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

bifurcation_diagram(x_0=0.6,n_0=0, n_f=400,step_size=0.05)

plt.show()

#%%

#Part 3, extending the plot to cover
# mu = 1....4 with step size of 0.005
plt.figure()

ax = plt.gca()

ax.set_title("Bifurcation Diagram $x_{n}$ vs. $\mu$:\n\
where $\mu$ = 1 to 4 and Step Size = 0.005",\
family='monospace',size=14, weight='bold')

ax.set_xlabel('$\mu$ [au]',fontsize =14)
ax.set_ylabel('$x_{n}$ [au]',fontsize =14)

ax.set_ylim(bottom=0, top=1.05)
ax.set_xlim(left=1.0, right=4.00)

ax.set_xticklabels(ax.get_xticks(), family='monospace', fontsize=10)
ax.set_yticklabels(ax.get_yticks(), family='monospace', fontsize=10)

bifurcation_diagram(x_0=0.6,n_0=0, n_f=400,step_size=0.005)

plt.show()
