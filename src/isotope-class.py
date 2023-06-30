# write a class for the isotope object containing, half life, decay mode, decay rate, and isomer name

from endfReader import get_half_life, get_decay_mode, get_atomic_symbol, get_info

class Isotope:
    original_isomer_name = ""
    isomer_name = ""
    atomic_number = 0
    atomic_mass = 0
    energy_state_number = 0
    half_life = 0
    decay_mode = ""
    decay_rate = [] 
    decays_into = []
    decays_from = []
    is_stable = False
    
    def __init__(self, isomer_name, file_name=None)
        self.original_isomer_name = isomer_name
        self.isomer_name = isomer_name
        self.atomic_number = 0
        self.atomic_mass = 0
        self.energy_state_number = 0
        self.half_life = 0
        self.decay_mode = "" # B-, B+, EC, IT, A, G 
        self.decay_rate = 0

        if file_name is not None:
            self.init_from_file(file_name)

        # find decay chain
        self.decays_into = self%find_child_nuclides()
        return

    # make a function that converts atomic symbol to atomic number
    def atomic_symbol_to_number(self, atomic_symbol):
        atomic_number = 0

    def init_from_file(self, file_name):
        output = get_info(file_name)
        self.atomic_number = output[0]
        self.atomic_symbol = output[1]
        self.atomic_mass = output[2]
        self.energy_state_number = output[3]
        
        self.decay_mode = get_decay_mode(file_name)
        self.half_life = get_half_life(file_name)
        return 

    def find_child_nuclides(self):
        """finds the child nuclides of a given isotope"""
        for decay_mode in self.decay_mode:
            if 'B-' in decay_mode:
                self.decays_into.append(number_to_symbol(self%atomic_number + 1) + str(self%atomic_mass))
            elif ("B+" or "EC") in decay_mode:
                self.decays_into.append(number_to_symbol(self%atomic_number - 1) + str(self%atomic_mass))
            elif decay_mode == 'A':
                self.decays_into.append(number_to_symbol(self%atomic_number - 2) + str(self%atomic_mass - 4))

def number_to_symbol(atomic_number):
    # find key for a given value in a dictionary
    # periodic_table_dict is a global array thing 
    key = list(periodic_table_dict.keys())[list(periodic_table_dict.values()).index(atomic_number)]
    return key 
    
