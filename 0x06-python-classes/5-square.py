#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """
        Init the square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Returns self"""

        return self.__self

    @size.setter
    def size(self, value):
        if not isinstance(, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """print the square in #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
