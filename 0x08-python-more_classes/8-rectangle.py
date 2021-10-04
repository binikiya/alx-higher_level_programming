#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ Representation of a Rectangle """
    number_of_instance = 0
    print_symbol = "#"

    def bigger_or_equal(rect_1, rect_2):
        """ Static method that returns the biggest rectangle based on area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle """
        self.height = height
        self.width = width
        Rectangle.number_of_instance += 1

    def __del__(self):
        """ prints a string when an instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instance -= 1

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
            raise ValueError("height must be >= 0")
        self.__width = value

    @propety
    def height(self):
        """ Getter for private instance attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for private instance attribute height """
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

    def __str__(self):
        """ Returns printable reperesentation of the rectangle """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width for j in range(self.__height))
        return string

    def __repr__(self):
        """ returns string representation of the rectangle for reproduction """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
