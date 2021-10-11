#!/usr/bin/python3
"""
100-my_int.py
"""


class MyInt(int):
    """a class that inherits from int"""
    def __new__(cls, *args, **kwargs):
        """creates the new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
