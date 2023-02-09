#!/usr/bin/python3
"""A function that writes in JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename, "w", encoding="utf-8") as Wjsonfile:

        json.dump(my_obj, Wjsonfile)
