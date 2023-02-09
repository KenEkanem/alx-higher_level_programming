#!/usr/bin/python3
"""A function that convert to PDS"""

import json


def from_json_string(my_str):
    """Convert JSON to python data structure"""

    return json.loads(my_str)
