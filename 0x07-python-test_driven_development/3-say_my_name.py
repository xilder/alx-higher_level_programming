#!/usr/bin/python3
"""
a function to print the first name and last name

"""


def say_my_name(first_name, last_name=""):
    """Prints the first name and the last name

        Args:
            first_name: the first name
            last_name: the last name

        Returns: nothing

        Raises:
            TypeError: if the either of the args is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
