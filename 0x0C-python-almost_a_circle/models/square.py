#!/usr/bin/python3
"""Square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initializer"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = self.width

    @property
    def size(self):
        """get property"""
        return self.width

    @size.setter
    def size(self, value):
        """set value"""
        self.height = value
        self.width = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """update the class square"""
        attribute = ["id", "size", "x", "y"]
        i = 0

        if args is not None and len(args) > 0:
            for arg in args:
                if i < 4:
                    setattr(self, attribute[i], arg)
                    i += 1

        elif (kwargs is not None):
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary of square sign"""

        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y, })
