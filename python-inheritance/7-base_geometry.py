#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Base class with geometry methods."""

    def area(self):
        """Raise an exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter (for error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
