#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square
    Args: size - represents the size of the square defined
    """

    def __init__(self, size):
        if isinstance(size, int)
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
