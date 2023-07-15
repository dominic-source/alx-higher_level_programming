#!/usr/bin/python3

"""Module that has the base class for all other classes that will 
inherit from it

"""


class Base:
    """The base class named as Base for readability purposes"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization method"""
        if id is not None:
            self.id = id
        elif id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
