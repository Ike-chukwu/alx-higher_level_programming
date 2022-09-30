#!/usr/bin/python3
"""The class MyInt that inherits from int"""

class MyInt(int):
    """Defines the objects"""

    def __eq__(self, other):
        """False if two objects(int) are differents"""
        return int(self) != other


    def __ne__(self, other):
        """True if two objects(int) are the same"""
        return int(self) == other
