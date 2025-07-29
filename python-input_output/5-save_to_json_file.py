#!/usr/bin/python3
"""
5-save_to_json_file module
This module provides a function to serialize a Python object
and write it to a file using JSON format.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to be serialized.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
