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
def calculate_decay_list(initial_pop, decay_rate, time):
    final_pop_list = np.zeros((np.size(initial_pop),np.size(time)),dtype=float)
    for ii in range(np.size(time)):
        final_pop_list[:,ii] = calulate_decay(initial_pop, decay_rate, time[ii])
    return final_pop_list

# create a dictionary with isotope names and decay rates

