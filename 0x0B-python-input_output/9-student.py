#!/usr/bin/python3
"""
9-strudent.py
"""


class Student:
    """representation of class struden"""
    def __init__(self, first_name, last_name, age):
        """initializes student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a student instance"""
        return self.__dict__
