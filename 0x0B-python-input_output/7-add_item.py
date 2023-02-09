#!/usr/bin/python3
"""script that adds all argument to a python list"""

from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

argv.pop(0)
try:
    des = load_from_json_file("add_item.json")
    if des is None:
        save_to_json_file(argv, "add_item.json")
    else:
        des.extend(argv)
        save_to_json_file(des, "add_item.json")
except FileNotFoundError:
    save_to_json_file(argv, "add_item.json")
