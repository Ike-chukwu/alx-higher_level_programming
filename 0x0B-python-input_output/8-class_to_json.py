#!/usr/bin/python3
"""
Module to return a dictionary description for JSON serialization
"""

def class_to_json(obj):
    """Return the dictionary, is equivalent to JSON serialization"""
    return obj.__dict__
