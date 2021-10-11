#!/usr/bin/python3
"""
101-add_attribute.py
"""


def add_attribute(obj, att, value):
    """Adds a new attribute if it's possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
