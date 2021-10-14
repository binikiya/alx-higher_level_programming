#!/usr/bin/python3
"""
100-singly_linked_list.py
"""


class Node:
    """represents a Node in singly linked list"""
    def __init__(self, data, next_node=None):
        """initializes the node class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of the __data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter of the __data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter of __next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of __next_node"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")

    def __str__(self):
        """string representation of Node instance"""
        return str(self.__data)


class SinglyLinkedList:
    """represents a singly linked list"""
    def __init__(self):
        """initializes the singly Linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node into a sorted position"""
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """string representation of singlyLinkedList"""
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string
