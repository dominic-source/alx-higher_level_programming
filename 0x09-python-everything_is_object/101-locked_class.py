#!/usr/bin/python3

class LockedClass:

    """A locked class"""

    cn = 'LockedClass'

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(f"'{self.cn}' object has no attribute {name}")

    def __delattr__(self, name):
        if name != "first_name":
            raise AttributeError(f"'{self.cn}' object has no attribute {name}")
