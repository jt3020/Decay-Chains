# write regex that will find these lines in an endf file
# Parent half-life: 613.9 S 6                                          1 1451   19
# Decay Mode: B-                                                       1 1451   20
import re

def get_half_life(endf_file):
    """use regex to find the half life number in seconds"""
    with open(endf_file, 'r') as f:
        for line in f:
            if 'Parent half-life' in line:
                return float(re.findall(r'\d+\.\d+', line)[0])
    return None
def get_decay_mode(endf_file):
    """use regex to find decay mode in endf file"""
    with open(endf_file, 'r') as f:
        for line in f:
            if 'Decay Mode' in line:
                return re.findall(r'\w+-', line)[0]
    return None

#write a function that splits the file name into proton number and atomic symbol and the mass number

def get_atomic_symbol(file_path):
    """a function that splits the file name into proton number and atomic symbol and the mass number"""
    file_name = file_path.split('/')[-1]
    return file_name.split('_')[1]  

def get_info(filename):
    atomic_number = int(filename[4:7])
    atomic_symbol = str(filename[8:10])
    atomic_mass = int(filename[11:14])
    if filename[14] == "m":
        energy_state = int(filename[15])
    else:
        energy_state = 0
    return [atomic_number, atomic_symbol, atomic_mass, energy_state]

print(get_decay_mode('decay_data/dec-000_Nn_001.endf'))
print(get_half_life('decay_data/dec-000_Nn_001.endf'))
print(get_atomic_symbol('decay_data/dec-000_Nn_001.endf'))

# import os 
# print(os.listdir('decay_data/'))