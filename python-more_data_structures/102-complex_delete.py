#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return

    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for key in list_ord:
        print("{}: {}".format(key, a_dictionary[key]))
