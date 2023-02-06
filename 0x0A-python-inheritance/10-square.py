#!/usr/bin/python3
"""Contains a class that inherits from `BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from `Rectangle`"""

    def __init__(self, size):
        """inherits from class 'Rectangle'"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
