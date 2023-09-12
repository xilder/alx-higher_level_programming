#!/usr/bin/python3

"""a square subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size):
        """inits the Square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """string representation pf the square class"""

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
