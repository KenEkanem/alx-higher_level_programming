#!/usr/bin/python3
"""Contains a `BaseGeometry` class"""


class BaseGeometry():
    """An empty class"""
    pass

    def area(self):
        """Calculate the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
