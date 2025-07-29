#!/usr/bin/python3
"""
0-read_file module
This module contains a function that reads a UTF-8 text file and prints its content to stdout.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The path to the file to be read. Defaults to an empty string.

    Usage:
        read_file("my_file.txt")

    Note:
        You do not need to handle exceptions for file permissions or file existence.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
