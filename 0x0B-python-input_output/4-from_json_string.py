#!/usr/bin/python3
"""
The program returns an object represented by JSON
"""


def from_json_string(my_str):
    """Import JSON and uses 'load' to get the object"""
    import json
    return json.loads(my_str)
