#!/usr/bin/python3

"""writes text to a file"""


def write_file(filename="", text=""):
    """writes to a file

    Args:
        filename: path to the file to be written to
        text: text string to be written into file
    """

    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
