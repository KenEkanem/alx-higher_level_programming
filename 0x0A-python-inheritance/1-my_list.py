#!/usr/bin/python3
"""My list"""


class MyList(list):
    """prints the sorted list"""
    def print_sorted(self):
        print(sorted(self))
