'''Edit the functions in this file as you complete the associated tasks.
Each test should utilise aspects of your code to complete the specified task.
These functions will be called by tests in the test suite to ensure you code is working properly.
'''

import numpy as np

class ElementInfo:
    atomic_number = {"H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10, "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17,"Ar":18, "K": 19, "Ca": 20, "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30, "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40, "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49, "Sn": 50, "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60, "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70, "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80, "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85, "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90, "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100, "Md": 101, "No": 102, "Lr": 103, "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109, "Ds": 110, "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116, "Ts": 117, "Og": 118}

    def get_atomic_number(self, element: str):
        return self.atomic_number[element]

    def get_atomic_symbol(self, atomic_number: int):
        for key, value in self.atomic_number.items():
            if value == atomic_number:
                return key
        else:
            return None


def nuclear_data_to_filename(atomic_number: int, atomic_mass: int, energy_state: int = 0):
    element_info = ElementInfo()
    filename = "dec-{}_{}_{}".format(str(atomic_number).zfill(3), element_info.get_atomic_symbol(atomic_number), str(atomic_mass).zfill(3))
    if energy_state != 0:
        filename += "m{}".format(str(energy_state))
    else:
        filename = filename
    filename += ".endf"
    return filename


def nuclear_data_to_isomer_name(atomic_number: int, atomic_mass: int, energy_state: int = 0):
    element_info = ElementInfo()
    isomer_name = "{}{}".format(element_info.get_atomic_symbol(atomic_number), atomic_mass)
    if energy_state:
        isomer_name += "m{}".format(energy_state)
    return isomer_name


def isomer_name_to_nuclear_data(isomer_name: str):
    element_info = ElementInfo()
    for index, char in enumerate(isomer_name):
        if char.isnumeric():
            string_index = index
            break

    atomic_symbol = isomer_name[:string_index]
    atomic_number = element_info.get_atomic_number(atomic_symbol)
    atomic_mass = int(isomer_name[string_index:].split("m")[0])
    try:
        energy_state = int(isomer_name[string_index:].split("m")[1])
    except IndexError:
        energy_state = 0

    return atomic_number, atomic_mass, energy_state

print(nuclear_data_to_filename(atomic_number=6, atomic_mass=13,energy_state=1))
print(nuclear_data_to_isomer_name(atomic_number=6, atomic_mass=13,energy_state=1))
print(isomer_name_to_nuclear_data("Cu70m2"))

def task_0_always_return_0():
    '''This function should always return the value zero'''
    return 0 + 0 + 0 + 1 - 1


def task_0_addition(a, b):
    '''This function should return the sum of the parameters a and b'''
    return a + b


def task_1a_simple_decay_chain_populations(output_times: list, initial_number_of_moles: float, decay_rate: float):
    '''
    Edit this function as part of Activity 1A
    This function should return the populations of two isomers at a number of output times as one decays into the other
    :param output_times: list array of floats containing the times at which the populations of the isomers should be returned. The first time will always be 0.
    :param initial_number_of_moles: The initial number of moles of Isomer 1 (the decaying isomer). Isomer 2 (the produced isomer) should have an initial population of 0.
    :param decay_rate: The decay rate of the decaying isomer in units of 1/s.
    :returns: Should return two sequences (e.g. lists, Tuples, 1D Numpy arrays) of length n where n is the number of output times. The first sequence contains the populations of Isomer 1 as a function of time, the second contains he populations of Isomer 1 as a function of time. Ine ach sequence, the value with index [0] in each array is the population the isomer at t=0 and the value with index [n] is the number of moles of the isomer at the end of the simulation.
    '''
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

    output = calculate_decay_list([initial_number_of_moles,0],[decay_rate,0],output_times)

    return output[0], output[1]


def task_1b_decay_data_from_filename(filepath: str):
    '''
    Edit this function as part of Activity 1B
    This function should accept the a filename of a file in the endf dataset and return its decay rate and decay mode
    :param filename: str containing the filename to be read from, with no path prefix (such as "dec-019_K_040.endf")
    :returns: Should be a tuple containing the decay rate as a float units of 1/s, and the change to the atomic number and atomic mass caused by the decay as ints (e.g. (1.0, -2, 4) for alpha decay with a decay rate of 1.0/s)
    '''
    pass


def task_1c_endf_filename_from_nuclear_data(atomic_number: int, atomic_mass: int, energy_state: int):
    '''
    Edit this function as part of Activity 1C
    This function should accept the nuclear data of a isomer and return the corresponding endf file name (without any preceding path)
    Note, you do not need to check if the file actually exists
    :param atomic_number: int providing the atomic number
    :param atomic_mass: int providing the atomic mass
    :param energy state: int providing the energy_state_number
    :returns: Should be a string containing the endf filename  corresponding to the nuclear data (without any preceding path), e.g. dec-006_C_016
    '''

    result = nuclear_data_to_filename(atomic_number,atomic_mass,energy_state)
    return result


def task_1c_isomer_name_from_nuclear_data(atomic_number: int, atomic_mass: int, energy_state: int):
    '''
    Edit this function as part of Activity 1C
    This function should accept the nuclear data of a isomer and return the corresponding isomer name
    :param atomic_number: int providing the atomic number
    :param atomic_mass: int providing the atomic mass
    :param energy state: int providing the energy_state_number
    :returns: Should be a string containing the isomer name  corresponding to the nuclear data, e.g. C16m1
    '''

    result = nuclear_data_to_isomer_name(atomic_number,atomic_mass,energy_state)
    return result


def task_1c_isomer_nuclear_data_from_name(isomer_name: str):
    '''
    Edit this function as part of Activity 1C
    This function should accept the name of an isomer and return its nuclear data
    :param isomer_name: str containing the name of the nucleus (e.g. "Na24m1")
    :returns: Should be a tuple containing the atomic number, atomic mass and energy state number as ints
    '''
    result = isomer_name_to_nuclear_data(isomer_name)
    return result


def task_2a_isomer_chain_from_initial_population(initial_isomer_name: str, initial_isomer_population: float, output_times: list):
    '''
    Edit this function as part of Activity 2A
    This function should accept the name of an isomer and return the populations of this and all daughter isomer sas a function of time
    :param isomer_name: str containing the name of the nucleus (e.g. "Na24m1")
    :param initial_isomer_population: float The number of moles of the initial isomer present
    :param output_times: list[float] The times at which the populations of isomers should be calculated. The first value will always be 0.
    :returns: Should be a dict whose keys are the names of the daughter isomers, and whose values are sequences (lists, tuple, numpy arrays, etc) holding the populations of those isomers at the output times
    '''
    pass
