#!/usr/bin/python3


"""100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding='UTF-8') as f:
        text = ""
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w', encoding='UTF-8') as f: 
        f.write(text)
