#!/usr/bin/python3

"""appends text to a file"""


def append_write(filename="", text=""):
    """writes to a file

    Args:
        filename: filepath
        text: text string to be appended
    """

    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
