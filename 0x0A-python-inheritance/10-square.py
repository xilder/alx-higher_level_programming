#!/usr/bin/python3

"""a square subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """inits the Square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area"""
        return self.__size * self.__size
    def __str__(self):
        """returns the string representation of Square"""
        return 
