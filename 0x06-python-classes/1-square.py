#!/usr/bin/python3

""" square docstings.

   This module tries to define a square from the previous square
   module (0-square).

   Example:
      $ ./1-square.py
"""

class Square:
    """create a private attribute

    Args:
        size(int): this is the size of the square

    Attributes:
        size(int): this is a private attribute

    """
    def __init__(self, size):
        """ the __init__ method

        Args:
            size: a private instance attribute

        """
        self.__size = size
