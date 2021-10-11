#!/usr/bin/python3
"""
1-my_list.py
"""

class MyList(list):
    """A subclass of list"""
    def __init__(self):
        """initializes an object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
