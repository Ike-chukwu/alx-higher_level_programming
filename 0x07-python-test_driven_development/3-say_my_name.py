#!/usr/bin/python3
"""
Function to print a phrase
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a phrase with:

    first_name: string to be printed
    last_name: second string to be printed

    Return: A formatted output with the strings.
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
