#!/usr/bin/python3
"""
Module that defines the function lookup(obj):
Returns a list of available attributes and methods of an object.
"""

def lookup(obj):
    return dir(obj)
