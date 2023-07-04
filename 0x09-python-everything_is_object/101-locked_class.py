#!/usr/bin/python3

"""This module will lock the class

"""


class LockedClass:

    """A locked class"""

    def __setattr__(self, n, value):

        """Set Attribute method which is always called"""

        if n != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{n}'")

    def __delattr__(self, n):

        """delete attribute method which is also when deleting attribute"""

        if n != "first_name":
            raise AttributeError(f"'Lockedclass' object has no attribute '{n}'")
