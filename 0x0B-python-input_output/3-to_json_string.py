#!/usr/bin/python3
"""it returns the string representation of an objeect"""
import json


def to_json_string(my_obj):
    """returns the json representation of an object

        Args:
            my_obj: the object to be represented in json format
    """
    return json.dumps(my_obj)
