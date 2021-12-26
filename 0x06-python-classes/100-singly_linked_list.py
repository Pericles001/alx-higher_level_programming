#!/usr/bin/python3
"""Class defined for a singly linked list"""

class Node:
    """Represents a node in a singly linked list"""
    
    def __init__(self, data, next_node=None):
        """Initialize a new node
        
            Args:
                data (int): The data of the new node
                next_node (Node): The next node after current one
        """
        
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter or setter for the data of node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value


    @property
    def next_node(self):
        """Getter or setter for the next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list"""

    def __init__(self):
        """Initialize a new singly linked list"""
        self.__head = None