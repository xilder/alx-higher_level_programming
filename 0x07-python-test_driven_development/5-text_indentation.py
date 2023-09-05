#!/usr/bin/python3

"""

A printing function that creates two new lines after every '.', '?' and ':'

"""


def text_indentation(text):
    """Inserts two newlines after every '.', '?', and ':'

    Args:
        text: the string to be printed

    raises:
        TypeError: if text isn't a string

    Return: nothing
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = 0
    flag = 0
    for i in range(len(text)):
        if text[i] not in ".?:":
            if text[i] == " ":
                count += 1
            elif text[i] == "\n":
                print(" " * count * flag + text[i], end="")
                flag = 0
            else:
                print(" " * count * flag + text[i], end="")
                flag = 1
                count = 0
        else:
            print(text[i] + "\n\n", end="")
            flag = 0
            count = 0
