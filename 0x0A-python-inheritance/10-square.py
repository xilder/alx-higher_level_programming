#!/usr/bin/python3

"""a rectangle subclass called square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """inits the Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
