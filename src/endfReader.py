
import re
import os
from string import ascii_lowercase
data_path = "decay_data"

def extract_decay_mode_info(line):
    pattern = r"Decay Mode:([^:]+)"
    match = re.search(pattern, line)
    if match:
        decay_mode = match.group(1).strip()
        return decay_mode
    else:
        return None

def remove_non_numeric(text):
    numeric_chars = []
    prev_char_is_digit = False

    for char in text:
        if char.isdigit():
            numeric_chars.append(char)
            prev_char_is_digit = True
        elif prev_char_is_digit:
            break

    return ''.join(numeric_chars)

def parse_string(list_of_strings):
    """loop through the strings, if the string is a number, convert it to a float and insert it as a value to the 
    to the previous key, otherwise the key stays 100, if there is an = sign then the key is the string before the = sign
    and the value is what is after"""
    decay_dict = {}
    for index, string in enumerate(list_of_strings):
        if "=" in string:
            string = string.split("=")
            decay_dict[string[0]] = float(remove_non_numeric(string[1]))
            continue
        if string.lower() in ascii_lowercase:
            decay_dict[string] = 100
            continue
        if "%" in string:
            decay_dict[list_of_strings[index - 1]] = float(string.strip("%,"))
            continue
    return decay_dict


def get_half_life(endf_file):
    """use regex to find the half life number in seconds"""
    with open(os.path.join(data_path, endf_file), 'r') as f:
        for line in f:
            if 'Parent half-life' in line:
                if "stable" in line.lower():
                    return 0
                return float(re.findall(r'\d+\.\d+', line)[0])
    return None

def get_decay_mode(path):
    """a function that extracts the decay mode and percentage from a line in the endf file, take into
    account multiple decay modes and percentages, return them in a dictionary"""

    with open(os.path.join(data_path, path), 'r') as f:
        for line in f:
            if 'Decay Mode' in line:
                decay_dict = parse_string(extract_decay_mode_info(line).split()[:-3])
                return decay_dict
    return None


def get_atomic_symbol(file_path):
    """a function that splits the file name into proton number and atomic symbol and the mass number"""
    file_name = file_path.split('/')[-1]
    return file_name.split('_')[1]  

def get_info(filename):
    atomic_number = int(filename[4:7])
    atomic_symbol = str(filename[8:10])
    atomic_mass = int(filename[11:13])
    if filename[14] == "m":
        energy_state = int(filename[15])
    else:
        energy_state = 0
    return [atomic_number, atomic_symbol, atomic_mass, energy_state]

import os
files = os.listdir('decay_data/')
decays = []
if __name__ == "__main__":
    for index, file in enumerate(files):
        path = os.path.join('decay_data', file)
        decay = get_decay_mode(path)
        print(decay)
        if index == 100:
            break
