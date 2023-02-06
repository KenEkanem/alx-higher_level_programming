#!/usr/bin/python3
"""Contains a class that inherits from `BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from `BaseGeometry `"""

    def __init__(self, width, height):

        """Initialize rectangle value"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calsulate the area of the geometry"""

        return (self.__width * self.__height)

    def __str__(self):
        """prints the area"""

        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
