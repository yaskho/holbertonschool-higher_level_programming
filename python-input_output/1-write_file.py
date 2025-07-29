#!/usr/bin/python3
"""
1-write_file module
This module contains a function that writes a string to a UTF-8 text file
and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The file path where the text will be written.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.

    Note:
        - The file is created if it does not exist.
        - The file content is overwritten if it already exists.
        - No exceptions related to file permissions need to be handled.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
