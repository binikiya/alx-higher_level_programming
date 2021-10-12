#!/usr/bin/python3
"""
8-class_to_json.py
"""


def class_to_json(obj):
    """returns dictionary discription with simple data structure"""
    return obj.__dict__
