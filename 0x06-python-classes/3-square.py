#!/usr/bin/python3

"""module that helps us understand the private instance attribute

It has the a square class with a private instance attribute

Example:
    $./3-square.py

"""


class Square:

    """defines what the class

    This includes the __init__ method and a private instance attribute

    Args:
       size (int): the values for the argument

    Attributes:
       size (int): the private instance attribute

    """

    def __init__(self, size=0):

        """Object initialization

        This will initialize the class object once instantiated

        Args:
            size (int): the size of the square

        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        """Calculate the area

        This method will calculate the area

        """

        return self.__size * self.__size
