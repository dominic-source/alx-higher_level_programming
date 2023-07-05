#!/usr/bin/python3

"""Square module

This module wil print the square of '#'

"""


def print_square(size=None):

    """Print a square of #"""

    if (size is None) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0) and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for m in range(size):
        for i in range(size):
            print('#', end='')
        print()
