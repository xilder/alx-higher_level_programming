#!/usr/bin/python3

"""this function reads a file"""


def read_file(filename=""):

    """opens a file and prints it

        Args:
            filename: path to to the filename to be opened
            """
    with open(filename, 'r', encoding='UTF-8') as f:
        file_content = f.read()
        print(file_content, end="")
