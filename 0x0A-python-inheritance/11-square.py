#!/usr/bin/python3
"""
11-square.py
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass of Rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """informal representation of string"""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
