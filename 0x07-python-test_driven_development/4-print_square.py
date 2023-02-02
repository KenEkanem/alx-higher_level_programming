#!/usr/bin/python3
# prints a square with the character #

def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (type(size) == float) < 0:
        raise TypeError("size must be an integer")

    print((("#" * size) + '\n') * size, end=("" if size else "\n"))
