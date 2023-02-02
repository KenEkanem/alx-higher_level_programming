#!/usr/bin/python3
#prints user firstname and lastname

def say_my_name(first_name, last_name=""):
    """Print firstname appended with lastname, raises error is name is not a string"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
