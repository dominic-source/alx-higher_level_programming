#!/usr/bin/python3

"""Module that checks if it inherit a subclass

"""


def inherits_from(obj, a_class):

    """inherits from another class

    checks if the obj inherit directly of indirectly from a_class

    """

    if obj.__class__.__base__ is a_class or isinstance(type(obj), a_class):
        return True
    return False
