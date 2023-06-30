class ElementInfo:
    atomic_number = {"H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10, "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "K": 19, "Ca": 20, "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30, "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40, "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49, "Sn": 50, "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60, "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70, "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80, "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85, "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90, "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100, "Md": 101, "No": 102, "Lr": 103, "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109, "Ds": 110, "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116, "Ts": 117, "Og": 118}

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