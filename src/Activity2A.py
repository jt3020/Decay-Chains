import numpy as np

def calulate_decay(initial_pop, decay_rate, time):
        # calculates the final populations of the two isotopes
        # for a given time float value
        final_pop = np.zeros(np.size(initial_pop),dtype=float)
        for ii in range(np.size(initial_pop)):
            if ii == 0:
                final_pop[ii] = initial_pop[ii] * np.exp(-decay_rate[ii] * time)
                decay_value = initial_pop[ii] - final_pop[ii]
            else:
                final_pop[ii] = (initial_pop[ii]+decay_value) * np.exp(-decay_rate[ii] * time)
                decay_value = (initial_pop[ii]+decay_value) - final_pop[ii]
        return final_pop
    
# return a list of final populations for each isotope for a list of times using the calculate_decay function
def calculate_decay_list(initial_pop, decay_rate, time):
    final_pop_list = np.zeros((np.size(initial_pop),np.size(time)),dtype=float)
    for ii in range(np.size(time)):
        final_pop_list[:,ii] = calulate_decay(initial_pop, decay_rate, time[ii])
    return final_pop_list

# create a dictionary with isotope names and decay rates
    
def create_decay_dict(isotope_names, decay_rates):
    decay_dict = {}
    for ii in range(np.size(isotope_names)):
        decay_dict[isotope_names[ii]] = decay_rates[ii]
    return decay_dict

def exercise_2a(decay_dict, isotope_pop, time):
    # create a list of isotope names and decay rates
    isotope_names = list(decay_dict.keys())
    decay_rates = list(decay_dict.values())
    
    # create a list of initial populations
    initial_pop = np.zeros(np.size(isotope_names),dtype=float)
    initial_pop[0] = isotope_pop
    
    # calculate the final populations for each isotope
    final_pop_list = np.zeros((np.size(initial_pop),np.size(time)),dtype=float)
    final_pop_list = calculate_decay_list(initial_pop, decay_rates, time)
    
    # print the final populations
    final_pop_dict = {}
    for ii in range(np.size(isotope_names)):
        final_pop_dict[isotope_names[ii]] = final_pop_list[ii,:]
        print(f' For Isotope {isotope_names[ii]}; values are: {final_pop_dict[isotope_names[ii]]}')

# Create decay dict for testing 2A (later use luis' code)
isotope_names = ['H','He','Li','Be','B','C','N','O','F','Ne']
decay_rates = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
decay_dict = create_decay_dict(isotope_names, decay_rates)

isotope_pop = 10.0
time = np.array([1,2,3],dtype=float)

exercise_2a(decay_dict, isotope_pop, time)





