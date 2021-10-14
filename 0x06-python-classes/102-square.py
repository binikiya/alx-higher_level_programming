#!/usr/bin/python3
""" Definition of a square class """


class Square:
    """ Representation of square class """
    def __init__(self, size=0):
        """ Initialization of square """
        self.size = size

    def area(self):
        """ Calculates the square's area """
        return (self.__size) ** 2

    @property
    def size(self):
        """ getter of __size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of __size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, other):
        """compares if square is less than others by area"""
        return self.size < other.size

    def __le__(self, other):
        """compares if square is less than or equal to others by area"""
        return self.size <= other.size

    def __eq__(self, other):
        """compares if square is equal to others by area"""
        return self.size == other.size

    def __ne__(self, other):
        """compares if square is not equal to other by area"""
        return self.size != other.size

    def __gt__(self, other):
        """compares if square is grater than others by area"""
        return self.size > other.size

    def __ge__(self, other):
        """compares if square is grater than or equal to others by area"""
        return self.size >= other.size
