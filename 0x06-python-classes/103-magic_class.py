#!/usr/bin/python3

"""Module to implement a magic class dissassembly

"""

import math


class MagicClass:
    """The magic class

    """

    def __init__(self, radius=0):

        """The initialization function

        This initialization is for our dissassembly class

        Args:
            radius (int|float): the radius of a circle

        """

        if not ((type(radius) is int) or (type(radius) is float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):

        """The area of a circle

        Here is the area of the circle

        """

        return ((self.__radius ** 2) * math.pi)

    def circumference(self):

        """The circumference of the circle

        Here is the circumference of the circle

        """

        return ((2 * math.pi) * self.__radius)
