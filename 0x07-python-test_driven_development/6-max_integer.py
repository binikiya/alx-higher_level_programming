#!/usr/bin/python3
"""
6-max_integer.py
"""


def max_integer(list=[]):
    """function to find max integer"""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
