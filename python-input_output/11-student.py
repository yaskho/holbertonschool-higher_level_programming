#!/usr/bin/python3
"""
Defines the Student class with serialization and deserialization capabilities.
"""

class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the instance.

        Args:
            attrs (list, optional): List of strings representing attribute names
                                    to include. If None, all attributes are included.

        Returns:
            dict: Dictionary representation of the student.
        """
        if isinstance(attrs, list) and all(type(attr) is str for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary with keys as attribute names and values as values.
        """
        for key in json:
            setattr(self, key, json[key])
