#!/usr/bin/python3
"""
Class BaseGeometry based in the last task
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """init objects"""
    def __init__(self, width, height):
        """Arguments would be checked by 'integer_validator()"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Representation of the object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
