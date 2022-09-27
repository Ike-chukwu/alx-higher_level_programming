#!/usr/bin/python3
"""
Checks if the object is an instance of, or if the
object is an instance of a class that inherited
from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """Using the 'isinstance()' method"""
    return isinstance(obj, a_class)
