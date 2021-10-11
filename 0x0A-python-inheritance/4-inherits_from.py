#!/usr/bin/python3
"""
4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """returns True if the obj is an instance of a_class that inherited from"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
