#!/usr/bin/python3
"""
Creates an object from a JSON file
"""

def load_from_json_file(filename):
    """Creates an object in a safe way"""
    import json
    with open(filename, encoding='utf-8') as fd:
        return json.load(fd)
