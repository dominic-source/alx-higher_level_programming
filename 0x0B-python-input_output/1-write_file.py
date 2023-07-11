#!/usr/bin/python3


"""Module that writes to file using a function

"""


def write_file(filename="", text=""):
    """Writes to the filename the string in text

    """

    with open(filename, encoding='utf-8', mode='w') as f:
        count = f.write(text)
    return count
