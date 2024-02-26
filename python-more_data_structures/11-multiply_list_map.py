#!/usr/bin/python3

def multiply_list_map(lst, multiplier):
    """
    Multiplies each element of the list by the multiplier using map function.
    """
    def multiply(x):
        return x * multiplier
    
    return list(map(multiply, lst))
