#!/usr/bin/python3


"""Module that create a geometry

"""


class BaseGeometry:

    """The base Geometry class

    """

    def area(self):
        """raise an exception

        a method that raises an exception when called

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name=None, value=None):
        """validate integers

        this will validate integers

        """
        if name is None:
            return
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
