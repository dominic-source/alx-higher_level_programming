#!/usr/bin/python3

"""This module will lock the class

"""


class LockedClass:

    """A locked class"""

    __allowed_attribute = {"first_name"}

    def __init__(self):

        """init function"""

        pass

    def __setattr__(self, nm, value):

        """Set Attribute method which is always called"""

        if nm not in self.__allowed_attribute:
            cl = self.__class__.__name__
            raise AttributeError(f"'{cl}' object has no attribute '{nm}'")
        else:
            object.__setattr__(self, nm, value)
