#!/usr/bin/python3

"""This module will lock the class

"""


class LockedClass:

    """A locked class"""

    def __init__(self):

        """init function"""

        pass

    def __setattr__(self, nm, value):

        """Set Attribute method which is always called"""

        if nm != "first_name":
            cl = "LockedClass"
            raise AttributeError(f"'{cl}' object has no attribute '{nm}'")

    def __delattr__(self, nm):

        """delete attribute method which is also when deleting attribute"""

        if nm != "first_name":
            cl = "LockedClass"
            raise AttributeError(f"'{cl}' object has no attribute '{nm}'")
