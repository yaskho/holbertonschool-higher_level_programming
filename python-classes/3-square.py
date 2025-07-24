#!/usr/bin/python3
"""Module that defines a Square with area method."""


class Square:
    """Represents a square with size and area method."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
