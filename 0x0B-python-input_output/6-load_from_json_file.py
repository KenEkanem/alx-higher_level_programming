#!/usr/bin/python3
"""creates an object from a JSON file"""

import json


def load_from_json_file(filename):
    """create a python object from json"""

    with open(filename, "r", encoding="utf-8") as f:

        obj = json.load(f)
        return obj
