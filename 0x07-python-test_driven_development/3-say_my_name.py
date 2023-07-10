#!/usr/bin/python3

"""Module that prints fullname

The function in the module will print the first and last name

"""


def say_my_name(first_name=None, last_name=""):

    """Say my first and last name"""

    if (first_name is None) or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
