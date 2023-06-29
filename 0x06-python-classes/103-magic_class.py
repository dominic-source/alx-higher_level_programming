#!/usr/bin/python3

"""Module to implement a magic class dissassembly

"""


class MagicClass:
    """The magic class

    """

    def __init__(self, radius=0):

        """The initialization function

        This initialization is for our dissassembly class

        Args:
            radius (int|float): the radius of a circle

        """

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):

        """The area of a circle

        Here is the area of the circle

        """

        return (self.radius ** 2) * math(pi)

    def circumference(self):

        """The circumference of the circle

        Here is the circumference of the circle

        """
        return ((2 * math(pi)) * self.radius)
