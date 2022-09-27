#!/usr/bin/python3

"""
Checks if an object is an instance of a class
that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """'issubclass()' used to check"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
