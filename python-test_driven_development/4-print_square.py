#!/usr/bin/python3
"""
Module 4-print_square
Defines a function that prints a square with the character #.
"""

def print_square(size):
    """
    Prints a square of size `size` with the character '#'.

    Args:
        size (int): The size of the square (length of each side).

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
