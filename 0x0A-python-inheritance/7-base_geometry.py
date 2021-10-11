#!/usr/bin/python3
"""
7-base_geometry.py
"""


class BaseGeometry:
    """A class that have an area method"""

    def area(self):
        """raises an exceptin"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
