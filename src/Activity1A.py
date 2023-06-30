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

## initial populations of isotopes
## isotope names - luis' class code
## for two isotopes calculate the population
## want a time value

# function that takes the intial population of two isotopes, their respective decay rates and the time, printing their final populations to terminal
def decay_chain(initial_population, decay_rates, times):
    # initial population is a list of the initial populations of the isotopes
    # decay rates is a list of the decay rates of the isotopes
    # time is the time at which we want to calculate the final populations of the isotopes
    # final populations is a list of the final populations of the isotopes
    # final populations is a list of the final populations of the isotopes
    final_populations = []
    # loop over the initial populations
    for time in times:
        final_pops = []
        for i in range(len(initial_population)):
            # calculate the final population of the isotope
            final_population = initial_population[i] * np.exp(-decay_rates[i] * time)

            # amend the final populations list so isotope 1 decays to isotope 2
            if i == 1:
                final_population = initial_population[i] - final_population + initial_population[i-1]*(1-np.exp(-decay_rates[i-1] * time))
            # append the final population to the final populations list

            final_pops.append(final_population)
        final_populations.append(final_pops)
    # return the final populations list
    return final_populations
