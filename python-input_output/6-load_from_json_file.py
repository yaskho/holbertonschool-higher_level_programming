#!/usr/bin/python3
"""
6-load_from_json_file module
This module provides a function to deserialize a JSON file into a Python object.
"""

import json

def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
