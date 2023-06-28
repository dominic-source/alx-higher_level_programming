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

    def __init__(self, size=0, position=(0, 0)):

        """Object initialization

        This will initialize the class object once instantiated

        Args:
            size (int): the size of the square
            position (turple): a turple

        Attributes:
            size (int): the size of the square
            position (turple): a position in the square

        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):

        """Retrieve the position of the square

        This will retrieve the position of the square

        """

        return self.__position

    @position.setter
    def position(self, value):

        """Set the position of the square

        This will set the position of the squares

        Args:
            value (turple): a turple

        """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(value[0], int)) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(value[1], int)) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        """Calculate the area

        This method will calculate the area

        """

        return self.__size * self.__size

    def my_print(self):

        """Print the # size in square

        This method will print # in square size

        """

        m = 0
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                while m < self.__position[0]:
                    print(' ', end='')
                    m += 1
                m = 0
                for j in range(self.__size):
                    print('#', end='')
                print("")
