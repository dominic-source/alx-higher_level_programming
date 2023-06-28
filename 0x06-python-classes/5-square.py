#!/usr/bin/python3

"""module that helps us understand the private instance attribute

It has the a square class with a private instance attribute

Example:
    $./4-square.py

"""


class Square:

    """defines what the class

    This includes the __init__ method and a private instance attribute

    Args:
       size (int): the values for the argument

    Attributes:
       size (int): the private instance attribute

    """

    def __init__(self, size=0):

        """Object initialization

        This will initialize the class object once instantiated

        Args:
            size (int): the size of the square

        """
        self.__size = size

    @property
    def size(self):

        """retrieve the data

        This method will retrieve data from the class

        """
        return self.__size

    @size.setter
    def size(self, value):

        """Set the size of the object

        This method will set the size of the square

        Args:
            value (int): the value of size

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """Calculate the area

        This method will calculate the area

        """

        return self.__size * self.__size

    def my_print(self):

        """Print the # size in square

        This method will print # in square size

        """

        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print("")
