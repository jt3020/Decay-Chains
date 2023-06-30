import isotope_class

def find_decay_chain(parent_name, nuclide_dict):
    # start with parent nuclide
    children = [parent_name]
    while True: 
        current_nuclide = nuclide_dict[children[-1]]
        nuclide_is_stable = False 
        # TODO: check if nuclide is stable
        if len(current_nuclide.decays_into) == 0:
            nuclide_is_stable = True
        if nuclide_is_stable:
            break 
            # if it is stable, then we break out of loop 
        # we have a decaying nuclide
        # asume only one decay mode for now
        next_nuclide_name = current_nuclide.decays_into[0]
        children.append(next_nuclide_name)
        
    return children
