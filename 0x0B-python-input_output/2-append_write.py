#!/usr/bin/python3

"""This Module implement the append functionality of the open function

"""


def append_write(filename="", text=""):
    """Append text to file"""

    with open(filename, encoding='utf-8', mode='a') as f:
        return f.write(text)
