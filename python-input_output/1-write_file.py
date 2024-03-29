#!/usr/bin/python3
"""
Contains function that returns number of lines in text
"""


def write_file(filename="", text=""):
    """Writes string text file (UTF8) returns number text written."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
