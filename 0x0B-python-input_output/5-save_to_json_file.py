#!/usr/bin/python3
"""
The program writes an object to a text file, with JSON
"""

def save_to_json_file(my_obj, filename):
    """Writes in a safe way to a text file with JSON"""
    import json
    with open(filename, mode='w', encoding='utf-8') as fd:
        return json.dump(my_obj, fd)
