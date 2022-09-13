#!/usr/bin/python3
"""A module for working with squares.
"""

class Square:
    """Represents a square with for 4 equal sides
    """
    def __init__(self, size=0):
        """Initializes a Square with a given size.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def area(self):
        """Computes the area of this Square.
        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2
