#!/usr/bin/python3

"""This Module contains the implementation of
a rectangle shape

    Args:
        __width (int): This is the width of the rectangle
        __height (int): This is the height of the rectangle
        __x (int): the x value of the shape
        __y (int): the y value of the shape
        __id (int): the id of shape
"""


from models.base import Base


class Rectangle(Base):
    """The rectangle class which inherits from it parent class name Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize attributes from arguments"""

        self.id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(self.id)

    @property
    def width(self):
        """Get the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""

        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""

        self.__height = value

    @property
    def x(self):
        """Get the x value of the rectangle"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the x value of the rectangle"""

        self.__x = value

    @property
    def y(self):
        """Get the y value of the rectangle"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set the y value of the rectangle"""

        self.__y = value
