#!/usr/bin/python3

"""This module will lock the class

"""


class LockedClass:

    """A locked class"""

    def __setattr__(self, nm, value):

        """Set Attribute method which is always called"""

        cn = 'LockedClass'
        if nm != "first_name":
            raise AttributeError(f"'{cn}' object has no attribute '{nm}'")

    def __delattr__(self, nm):

        """delete attribute method which is also when deleting attribute"""

        cn = 'LockedClass'
        if nm != "first_name":
            raise AttributeError(f"'{cn}' object has no attribute '{nm}'")
