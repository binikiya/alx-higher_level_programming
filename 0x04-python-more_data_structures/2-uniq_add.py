#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for i in my_list:
        isFound = False
        for j in new_list:
            if i == j:
                isFound = True
        if not isFound:
            sum += i
            new_list.append(i)
    return (sum)
