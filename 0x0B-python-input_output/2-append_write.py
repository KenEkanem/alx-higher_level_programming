#!/usr/bin/python3
"""A function that write"""


def append_write(filename="", text=""):
    """Writes a string and return character length"""

    with open(filename, "a", encoding="utf-8") as Wfile:

        texts = len(text)
        Wfile.write(text)
        return texts
