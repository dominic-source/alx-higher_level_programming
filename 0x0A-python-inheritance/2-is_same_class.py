#!/usr/bin/python3

"""Module check for the instance of a class

"""


def is_same_class(obj, a_class):
    """an isinstance function

    Checks for an instance of the class similarity
    """

    if type(obj) is a_class:
        return True
    return False
