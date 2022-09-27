#!/usr/bin/python3
"""
The program returns a JSON representation of an object
"""

def to_json_string(my_obj):
    """JSON representation of an object"""
    import json
    return json.dumps(my_obj)
