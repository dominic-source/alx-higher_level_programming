#!/usr/bin/python3

"""module that defines a square

This module demonstrate how to use square private instance attributes

Example:
    $ ./2-square.py

"""


class Square:

    """defines the kind of attribute for a square class or object

    Args:
        size (int): this is the size of the square object

    Attributes:
        size (int): this is an attribute of the square object

    """

    def __init__(self, size=0):
        """object initialization

        This will initialize the class for each instance of the class

        Args:
            size (int): initialize the size of the class

        """

        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
