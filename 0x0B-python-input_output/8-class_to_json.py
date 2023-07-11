#!/usr/bin/python3

"""Module tha hold a function

Contains a function that returns a dictionary description

"""


def class_to_json(obj):
    """class to json function"""

    return obj.__dict__
