#!/usr/bin/python3
"""Function that returns the weighted average of all integers tuple.
"""


def weight_average(my_list=[]):
    """Function to return the weighted average of a list of tuples"""
    if not my_list:
        return 0
    total = 0
    total_weight = 0
    for tup in my_list:
        total += tup[0] * tup[1]
        total_weight += tup[1]
    return total / total_weight


if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("{:.1f}".format(result))
