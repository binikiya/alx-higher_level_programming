#!/usr/bin/python3
"""
9-rectangle.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class that is subclass of BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """informal string representation"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
