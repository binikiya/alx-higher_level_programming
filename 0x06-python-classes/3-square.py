#!/usr/bin/python3
""" Definition of square class """


class Square:
    """ Representation of square class """
    def __init__(self, size=0):
        """ Initialization of a square """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculates the square's area """
        return (self.__size) ** 2
