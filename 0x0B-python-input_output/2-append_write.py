#!/usr/bin/python3
"""
2-append_write.py
"""


def append_write(filename="", text=""):
    """appends a string at the end of the file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
