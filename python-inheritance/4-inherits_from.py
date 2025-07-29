#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, but not if obj is an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
