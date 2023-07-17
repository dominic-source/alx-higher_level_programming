#!/usr/bin/python3
"""This is the module uses square to inherit from the class rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class that inherit te properties and attributes of the
    rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square class"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""

        self.width = value
        self.height = value

    def to_dictionary(self):
        """Dictionary representation of a rectangle"""

        my_dict = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

        return my_dict

    def update(self, *args, **kwargs):
        """update the attribute of the class"""

        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        elif len(kwargs) != 0:
            if "id" in kwargs:
                self.id = kwargs['id']
            if "size" in kwargs:
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def __str__(self):
        """string representation"""

        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)
