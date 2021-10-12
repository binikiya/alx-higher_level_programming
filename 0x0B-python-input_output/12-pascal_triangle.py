#!/usr/bin/python3
"""
12-pascal_triangle.py
"""


def pascal_triangle(n):
    """returns lists of lists of integers representing the pascal's triangle"""
    if n <= 0:
        return []
    tri = [[1]]
    while tri != n:
        t = tri[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
