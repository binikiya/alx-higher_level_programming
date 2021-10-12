#!/usr/bin/python3
"""
1-write_file.py
"""


def write_file(filename="", text=""):
    """writes a string to a file & returns the no. of character written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
