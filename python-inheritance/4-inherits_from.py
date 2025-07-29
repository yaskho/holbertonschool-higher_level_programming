#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance of a
class that inherits from a specified class (excluding the class itself).
"""

def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherits (directly or
    indirectly) from a_class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
