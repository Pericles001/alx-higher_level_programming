#!/usr/bin/python3
"""Define a class Square"""

from typing import Sized, Type


class Square:
    """Represent a square"""
    
    def __init__(self, size=0):
        """Initialize a new square
        
            Args:
                size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Getter and setter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)


    def __eq__(self, other):
        """Define the == comparison to a square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a square"""
        return self.area != other.area()

    def __lt__(self, other):
        """Define the < comparison to a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison with a square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a square"""
        return self.area() >= other.area()
