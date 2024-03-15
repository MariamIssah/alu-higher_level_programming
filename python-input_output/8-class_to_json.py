#!/usr/bin/python3
""" function returns dictionary descripted simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:"""


def class_to_json(obj):
    """ Return the dictionary description of an object """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
