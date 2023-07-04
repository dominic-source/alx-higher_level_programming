#!/usr/bin/python3

"""This module will lock the class

"""


class LockedClass:

    """A locked class"""

    cn = 'LockedClass'

    def __setattr__(self, nm, value):

        """Set Attribute method which is always called"""

        if nm.lower() != "first_name":
            raise AttributeError(f"'{self.cn}' object has no attribute '{nm}'")

    def __delattr__(self, nm):

        """delete attribute method which is also when deleting attribute"""

        if nm.lower() != "first_name":
            raise AttributeError(f"'{self.cn}' object has no attribute '{nm}'")
