#!/usr/bin/python3

"""Implement a student module

"""


class Student:
    """A class to define student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the class
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """convert data to json"""

        if attrs is None:
            return self.__dict__
        elif not isinstance(attrs, list):
            return self.__dict__
        elif isinstance(attrs, list):
            for i in attrs:
                if not isinstance(i, str):
                    return self.__dict__
        new_list = []
        for i in attrs:
            if hasattr(self, i):
                new_list.append((i, self.__dict__[i]))
        return dict(new_list)
