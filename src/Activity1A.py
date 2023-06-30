import numpy as np

def calulate_decay(initial_pop, decay_rate, time):
        # calculates the final populations of the two isotopes
        # for a given time float value
        final_pop = np.zeros(np.size(initial_pop),dtype=float)
        for ii in range(np.size(initial_pop)):
            if ii == 0:
                final_pop[ii] = initial_pop[ii] * np.exp(-decay_rate[ii] * time)
            else:
                final_pop[ii] = initial_pop[ii] * np.exp(-decay_rate[ii] * time) + (initial_pop[ii-1] - final_pop[ii-1])
    
        return final_pop
    
# return a list of final populations for each isotope for a list of times using the calculate_decay function
def calculate_decay_list(initial_pop, decay_rate, time, final_pop_list):
    
    for ii in range(np.size(time)):
        final_pop_list[:,ii] = calulate_decay(initial_pop, decay_rate, time[ii])
    return final_pop_list

"""
For a given 1D array of:
    initial populations;
    decay rates;
    times

calculate the final populations of each isotope at each time using the calculate_decay_list function
as a 2D array of final populations of dimensions[isotope, time]

"""

initial_pop = np.array([2,0],dtype=float)
decay_rate = np.array([5,0],dtype=float)
time = np.array([0,0.5,1,2,3,4],dtype=float)
final_pop_list = np.zeros((np.size(initial_pop),np.size(time)),dtype=float)

final_pop_list[:,:] = calculate_decay_list(initial_pop, decay_rate, time, final_pop_list)
    

for ii in range(np.size(time)):
    print(f'At time {time[ii]} the final populations are {final_pop_list[:,ii]}')
