#!/usr/bin/python3

"""A module that implement adding an attribute

"""


def add_attribute(obj, attr, value):

    """Add attribute to the the class"""

    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
