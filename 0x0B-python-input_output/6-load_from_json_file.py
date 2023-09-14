#!/usr/bin/python3
"""a function that loads json string from a file"""
import json


def load_from_json_file(filename):

    """saves a json obj to a file

        Args:
            filename: filepath to store it
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        return json.load(f)
