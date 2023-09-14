#!/usr/bin/python3

"""a class that defines a student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """inits the class student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary representation of a
            student instance
            If attrs is a list of strings, represents only
            those attributes included in the list
        """
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            return {att: getattr(self, att) for att in attrs if hasattr(self, att)}
        return self.__dict__
