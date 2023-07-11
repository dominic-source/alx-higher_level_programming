#!/usr/bin/python3

"""A module that utilizes a functin to search and update file

"""


def append_after(filename="", search_string="", new_string=""):
    """Append after function"""

    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
