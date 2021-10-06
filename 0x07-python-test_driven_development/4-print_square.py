#!/usr/bin/python3
"""
4-print_square.py
"""


def print_square(size):
    """a function that prints square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
