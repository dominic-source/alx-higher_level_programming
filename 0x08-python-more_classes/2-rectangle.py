#!/usr/bin/python3


"""This is the rectangle module to further understand classes

"""


class Rectangle:

    """Rectangle class
    """

    def __init__(self, width=0, height=0):

        """Initialization function"""

        self.width = width
        self.height = height

    @property
    def width(self):

        """Get the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):

        """Set the width of the Rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """Get the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):

        """Set the value of the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """Returns the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):

        """Returns the perimeter of a rectangle"""

        if self.height == 0 or self.width == 0:
            return 0
        return (2 * (self.__height + self.__width))
