#!/usr/bin/python3

"""

a function to add attribute to a class if the can have atttribute

"""


def add_attribute(obj, attr, value):
    """adds an attribute to a class if the can have attributes"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't have attribute")
