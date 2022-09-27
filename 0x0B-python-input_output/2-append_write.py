#!/usr/bin/python3
"""
The function appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """append a string in the text file """
    with open(filename, mode='a', encoding='utf-8') as fd:
        string = fd.write(text)
    return string
