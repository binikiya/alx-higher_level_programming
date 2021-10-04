#!/usr/bin/python3
""" Definition of a square class """


class Square:
    """ Representation of a square class """
    def __init__(self, size=0):
        """ Initialization of a square """
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
    def my_print(self):
        """ prints the square """
        if self.__size == 0:
            print()
            return 0
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
