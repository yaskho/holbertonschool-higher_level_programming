#!/usr/bin/python3
"""
Defines a Student class with optional attribute filtering for JSON serialization.
"""

class Student:
    """
    A class representing a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, returns only those attributes
        listed in attrs that exist in the instance.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
