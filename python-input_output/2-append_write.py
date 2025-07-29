#!/usr/bin/python3
"""
2-append_write module
This module contains a function that appends a string to a UTF-8 text file
and returns the number of characters added.
"""

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The path to the file where the string will be appended.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.

    Note:
        - The file is created if it does not exist.
        - No need to handle file permission or existence exceptions.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
