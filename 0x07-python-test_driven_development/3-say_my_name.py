#!/usr/bin/python3

"""Module that prints fullname

The function in the module will print the first and last name

"""


def say_my_name(first_name="", last_name=""):

    """Say my first and last name"""

    if (first_name == "") or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if (last_name == "") or not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
