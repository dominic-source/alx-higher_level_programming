#!/usr/bin/python3

"""module documentation to lookup a list of available attributes

This module will lookup available attributes and methods of an object

"""


def lookup(obj):
    """This function returns a list attributes in the object

    """

    return dir(obj)


if __name__ == '__main__':
    lookup(int)
