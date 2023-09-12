#!/usr/bin/python3

"""An empty BaseGeometry class"""


class BaseGeometry:
    """represents a base geometry"""

    def area(self):
        """method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if a value is valid"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
