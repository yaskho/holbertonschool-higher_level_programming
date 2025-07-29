#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""


class BaseGeometry:
    """Base class for geometry-related operations."""

    def area(self):
        """Raises an exception indicating that area is not implemented."""
        raise Exception("area() is not implemented")
