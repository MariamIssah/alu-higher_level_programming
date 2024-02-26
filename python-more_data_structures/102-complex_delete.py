#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.
    """
    if not a_dictionary:  # Check if dictionary is empty
        return
    
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_delete:
        del a_dictionary[key]

# Tests
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ({'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}, 'a'),
        ({'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}, 'e'),
        ({'a': "a", 'b': "b", 'c': "c", 'd': "d", 'e': "e"}, 'f'),
        ({'a': "a", 'b': "b", 'c': "a", 'd': "a", 'e': "e"}, 'a'),
        ({'c': "a", 'd': "a"}, 'a'),
        ({}, 'a')
    ]

    for my_dict, value in test_cases:
        print("Original Dictionary:", my_dict)
        complex_delete(my_dict, value)
        print("Dictionary after deletion:", my_dict)
        print()

