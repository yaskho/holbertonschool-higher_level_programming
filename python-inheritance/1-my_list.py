#!/usr/bin/python3
"""Module that defines the MyList class"""


class MyList(list):
    """A subclass of list that includes a method to print a sorted version."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
