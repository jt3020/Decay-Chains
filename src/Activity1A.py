import numpy as np

#write a forward Euler solver for the decay chain
def forward_euler_solver(decay_rates, initial_population, stoptime):
    '''
    This function should accept the decay rates of the isomers in a decay chain, the initial population of the first isomer, and the times at which the populations of the isomers should be calculated. It should return the populations of the isomers at the output times.
    :param decay_rates: dict[str, float] whose keys are the names of the isomers, and whose values are the decay rates of those isomers
    :param initial_population: float The number of moles of the initial isomer present
    :param output_times: list[float] The times at which the populations of isomers should be calculated. The first value will always be 0.
    :returns: Should be a dict whose keys are the names of the isomers, and whose values are sequences (lists, tuple, numpy arrays, etc) holding the populations of those isomers at the output times
    '''

    #create a dictionary to store the populations of the isomers at the output times
    populations = []
    output_times = np.arrange(0, stoptime, 1000)
    #loop over the output times
    for time in output_times:
        #calculate the populations of the isomers at the current time
        #and store them in the populations dictionary
        newpop = 
        populations[time] = None
    #return the populations dictionary
    return populations
    pass