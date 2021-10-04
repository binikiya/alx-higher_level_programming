#!/usr/bin/python3
"""
1-matrix_divided.py
"""
def matrix_divided(matrix, div):
    """ divides all elements in the matrix by div """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(i)
        elif size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not int or type(j) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
        if type(div) is not int or type(div) is not float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        return [[round(i / div, 2) for j in i] for i in matrix]
