#!/usr/bin/python3
"""
5-text_indentation.py
"""
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i == '?' or i == '.' or i = ':':
                print(i)
                print()
                flag = 0
            else:
                print(a, end="")