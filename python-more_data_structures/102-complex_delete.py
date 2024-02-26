#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.
    """
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_delete:
        del a_dictionary[key]

# Test the function
if __name__ == "__main__":
    my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
    print("Original Dictionary:", my_dictionary)
    complex_delete(my_dictionary, 2)
    print("Dictionary after deletion:", my_dictionary)

