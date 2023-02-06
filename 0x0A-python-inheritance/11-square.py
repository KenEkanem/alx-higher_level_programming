#!/usr/bin/python3
"""A square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherit from class"""
    def __init__(self, size):
        """initialize the value"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Prints the descrition of the Rectangle"""
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
