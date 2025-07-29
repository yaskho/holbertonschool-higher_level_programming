#!/usr/bin/python3
"""
This module provides a function that converts an object to a dictionary
with only serializable attributes (simple data types).
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Args:
        obj: An instance of a class

    Returns:
        dict: A dictionary of serializable attributes
    """
    return obj.__dict__
