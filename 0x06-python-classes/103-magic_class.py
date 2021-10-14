#!/usr/bin/python3
"""
103-magic_class.py
"""
import math


class MagicClass:
    """this represents a magic class"""
    def __init__(self, radius=0):
        """initializes a Magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates area of a circle"""
        return math.pi * (self.__radius ** 2)

    def circumstances(self):
        """calculates circumstances of a circle"""
        return 2 * math.pi * self.__radius
