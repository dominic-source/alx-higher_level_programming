#!/usr/bin/python3

"""Modules that solves a rebellious task

"""


class MyInt(int):
    """The integer class inheritance practice"""

    def __init__(self, tni):
        """Initialize the class for learning purposes"""

        self.__tni = tni

    def __str__(self):
        """string representation of the class"""

        return str(self.__tni)

    def __eq__(self, other):
        """upside down implementation of equality"""

        if type(other) is int:
            return (other != self.__tni)
        return NotImplemented

    def __ne__(self, other):
        """upside down implementation of equality"""

        if type(other) is int:
            return (other == self.__tni)
        return NotImplemented
