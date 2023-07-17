#!/usr/bin/python3

"""This Module contains the implementation of
a rectangle shape

    Args:
        __width (int): This is the width of the rectangle
        __height (int): This is the height of the rectangle
        __x (int): the x value of the shape
        __y (int): the y value of the shape
        __id (int): the id of shape
"""


from models.base import Base


class Rectangle(Base):
    """The rectangle class which inherits from it parent class name Base"""

    def __init__(self, width=None, height=None, x=0, y=0, id=None):
        """initialize attributes from arguments"""
        
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x value of the rectangle"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the x value of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y value of the rectangle"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set the y value of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
    
        return self.width * self.height
    
    def to_dictionary(self):
        """Dictionary representation of a rectangle"""
        my_dict = {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
        return my_dict

    def display(self):
        """display characters for strings"""
        
        for i in range(self.y):
            if self.y != 0:
                print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end='')
            for m in range(self.width):
                print('#', end='')
            print()
    
    def __str__(self):
        """string representation"""

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update the attribute of the class"""

        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]
        elif len(kwargs) != 0:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "width" in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

