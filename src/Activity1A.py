import numpy as np

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