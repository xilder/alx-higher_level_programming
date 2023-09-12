#!/usr/bin/python3
"""A Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """A derived class"""
    def __init__(self, width, height):
        """initialises the object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """printable version"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
