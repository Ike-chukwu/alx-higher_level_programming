#!/usr/bin/python3
"""
A class that inherits from class 'list'
"""

class MyList(list):
    """Mylist - subclass of the class 'list'"""
    def print_sorted(self):
        """print_sorted - method to sort a list"""
        l = (sorted(self[:]))
        print(l)
