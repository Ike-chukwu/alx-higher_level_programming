#!/usr/bin/python3
"""
Function to print a square
"""

def print_square(size):
    """
    Prints a square using '#'
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print('#' * size)
