#!/usr/bin/python3

"""A rectangle module

Checks out a rectangle

"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class to practice inheritance

    """

    def __init__(self, width, height):
        """Initialization function called at the initiation of a function"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
