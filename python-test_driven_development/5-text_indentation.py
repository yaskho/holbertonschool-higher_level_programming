#!/usr/bin/python3
"""
This module provides a function for printing a text with
2 new lines after each of these characters: '.', '?', and ':'.

Function:
    text_indentation(text): Prints formatted text with 2 new lines
    after '.', '?', and ':'.
"""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The input string to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for char in text:
        if new_line and char == ' ':
            continue
        new_line = False

        print(char, end="")

        if char in ".:?":
            print("\n")
            new_line = True
