#!/usr/bin/python3

"""Module that adds two integers

This module will add two integers together and return an integer

Args:
    a (int): the first argument
    b (int): the second argument

"""


def add_integer(a=None, b=98):

    """Add two integers and returns the sum"""

    if (a is None) or not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (b is None) or not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
