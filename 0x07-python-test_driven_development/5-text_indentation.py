#!/usr/bin/python3
"""
5-text_indentation.py
"""


def text_indentation(text):
    """a function for text indentation"""
    if type(text) is not str:
        raise TypeError("text must be string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or i == '.' or a = ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
