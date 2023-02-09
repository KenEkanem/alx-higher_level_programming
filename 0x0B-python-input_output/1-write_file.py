#!/usr/bin/python3
"""A function that write"""


def write_file(filename="", text=""):
    """Writes a string and return character length"""

    with open(filename, "w", encoding="utf-8") as Wfile:

        texts = len(text)
        Wfile.write(text)
        return texts
