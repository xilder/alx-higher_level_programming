#!/usr/bin/python3
"""it returns a python object from a python string"""
import json


def from_json_string(my_str):
    """converts json strings from json to pyhton objects

        Args:
            my_str: string to be converted

        Return: a pyhton object
        """

    return json.loads(my_str)
