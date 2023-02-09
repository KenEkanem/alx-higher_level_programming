#!/usr/bin/python3
"""A function that reads in UTF-8"""


def read_file(filename=""):
    """A function that reads the text file"""
    with open(filename, encoding="utf-8") as Rfile:

        for line in Rfile:
            print(line, end="")
