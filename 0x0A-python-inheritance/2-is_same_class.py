#!/usr/bin/python3
"""
2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """return True if the object is exactly an instance of specified class"""
    return (type(obj) == a_class)
