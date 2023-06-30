# write a class for the isotope object containing, half life, decay mode, decay rate, and isomer name

class Isotope:
    original_isomer_name = ""
    isomer_name = ""
    atomic_number = 0
    atomic_mass = 0
    energy_state_number = 0
    half_life = 0
    decay_mode = ""
    decay_rate = 0
    def __init__(self, isomer_name):
        self.original_isomer_name = isomer_name
        self.isomer_name = isomer_name
        self.atomic_number = 0
        self.atomic_mass = 0
        self.energy_state_number = 0
        self.half_life = 0
        self.decay_mode = ""
        self.decay_rate = 0

    # make a function that converts atomic symbol to atomic number
    def atomic_symbol_to_number(self, atomic_symbol):
        atomic_number = 0


