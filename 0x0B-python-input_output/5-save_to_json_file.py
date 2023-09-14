#!/usr/bin/python3
"""a function that writes json string to a file"""
import json


def save_to_json_file(my_obj, filename):
    """saves a json obj to a file

        Args:
            my_obj: python object to be stored
            filename: filepath to store it
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
