#!/usr/bin/python3


"""100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a new string in the next line if it the
        search_string is present in the file
    """

    text = ""
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w', encoding='UTF-8') as h:
        h.write(text)
