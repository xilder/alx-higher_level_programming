#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
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
        for i in position:
            if i < 0:
                raise TypeError("position must be a tuple " +
                "of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a "
                  +  "tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Returns size"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns position"""

        return self.__position

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a " + 
                        "tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """print the square in #"""

        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
