#!/usr/bin/python3

"""Module to test inheritance

This module makes clear an understand of inheritance

"""


class MyList(list):
    
    """MyList class to describe list object inheritance

    """

    def __init__(self):
        """initialize object MyList

        """
        super().__init__()

    def print_sorted(self):
        """Print a sorted list of the list of object

        """
        print(self.copy.sorted())


