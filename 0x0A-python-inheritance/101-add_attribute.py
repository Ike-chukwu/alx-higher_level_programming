#!/usr/bin/python3
"""Adds a new attribute to an object if it is possible"""

def add_attribute(clss, atrb, val):
    """Using the method 'setattr()' to add attributes"""
    if "__dict__" in dir(clss):
        setattr(clss, atrb, val)
    else:
        raise TypeError("can't add new attribute")
