#!/usr/bin/python3

"""Module that enables further understanding of inheritance

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class for a square

    """
    def __init__(self, size):
        """Initialize the square function"""

        self.integer_validator("size", size)
        super().__init__(size, size)
