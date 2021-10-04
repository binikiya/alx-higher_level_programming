#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ Representation of a Rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Getter for private instance attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for private instance attribute width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @propety
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if type(value) in not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
