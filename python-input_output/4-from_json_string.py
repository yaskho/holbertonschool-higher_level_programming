#!/usr/bin/python3
"""
4-from_json_string module
This module provides a function to deserialize a JSON string into a Python object.
"""

import json

def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python data structure.
    """
    return json.loads(my_str)
