#!/usr/bin/python3

"""This module will lock the class

"""


class LockedClass:

    """A locked class"""

    cn = 'LockedClass'

    def __setattr__(self, name, value):

        """Set Attribute method which is always called"""

        if name != "first_name":
            raise AttributeError(f"'{self.cn}' object has no attribute {name}")

    def __delattr__(self, name):

        """delete attribute method which is also when deleting attribute"""
        if name != "first_name":
            raise AttributeError(f"'{self.cn}' object has no attribute {name}")
