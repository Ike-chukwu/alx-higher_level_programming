#!/usr/bin/python3
"""
Class Square based in the last task
"""
Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """init objects"""
    def __init__(self, size):
        """Defines attributes"""
        self.integer_validator("size", size)
        self.__size = size


    def area(self):
        """Computes the area of a square"""
        return self.__size * self.

    def __str__(self):
        """Representation of a square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
