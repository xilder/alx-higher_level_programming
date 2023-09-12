#!/usr/bin/python3

"""

a function to add attribute to a class if the can have atttribute

"""


def add_attribute(obj, attr, value):
    """adds an attribute to a class if the can have attributes"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
