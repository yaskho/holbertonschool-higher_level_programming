#!/usr/bin/python3
"""
3-say_my_name module

This module contains a function `say_my_name` that prints a formatted string
introducing a person by their first and last names.

Functions:
- say_my_name(first_name, last_name=""): Prints "My name is <first_name> <last_name>".
  Raises TypeError if arguments are not strings.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}".strip())