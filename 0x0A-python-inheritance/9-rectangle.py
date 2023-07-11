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

        self.integer_validator(width, width)
        self.integer_validator(height, height)
        self.__width = width
        self.__height = height

    def area(self):

        """Implement the area method

        """

        return self.__width * self.__height

    def __str__(self):

        """string representation of the data"""

        string = "[" + self.__repr__() + "] " + str(self.__width)
        string += '/' + str(self.__height)

        return string

    def __repr__(self):

        """a representation of the class"""

        return "Rectangle"
