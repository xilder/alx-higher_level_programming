#!/usr/bin/python3
"""

Prints a square with the character '#'

"""


def print_square(size):
    """prints a square of size size with the character #

    Args:
        size: the size of the square

    Returns: nothing
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """


    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
