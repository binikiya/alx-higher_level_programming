#!/usr/bin/python3
"""
1-write_file.py
"""


def write_file(filename="", text=""):
    """writes a string to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
