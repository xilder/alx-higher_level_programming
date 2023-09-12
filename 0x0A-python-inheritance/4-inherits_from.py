#!/usr/bin/python3

"""Returns only true when obj is an instance of a_class subclass"""


def inherits_from(obj, a_class):
    """as defined above"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
