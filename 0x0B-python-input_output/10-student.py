#!/usr/bin/python3
"""
10-strudent.py
"""


class Student:
    """representation of class struden"""
    def __init__(self, first_name, last_name, age):
        """initializes student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student instance"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict
