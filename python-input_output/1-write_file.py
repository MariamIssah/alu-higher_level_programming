#!/usr/bin/python3
"""
Module 1-number_of_lines

Contains function that returns number of lines in text"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns number text written."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
