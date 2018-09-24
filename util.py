def is_valid_module(module_obj):
    """
    Check if `module_obj` implements the required functions and variables.
    """
    # Check for the existence and type of the required variables
    for var in [('NAME', 'str'), ('setup', 'function'), ('step', 'function')]:
        if var[0] not in dir(module_obj):
            return False
        if module_obj.__getattribute__(var[0]).__class__.__name__ != var[1]:
            return False

    # Return module as invalid if the hidden_module variable exists
    if 'hidden_module' in dir(module_obj):
        return False

    return True
