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


class Rectangle(Base):
    """The rectangle class which inherits from it parent class name Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize attributes from arguments"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id

    @property
    def width(self):
        """Get the width of the rectangle"""
        
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        
        self.__width = value

