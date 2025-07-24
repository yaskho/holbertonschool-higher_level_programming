#!/usr/bin/python3
"""Module that defines a Square with private size."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
