#!/usr/bin/python3
"""
Module for a class that prevents dynamic attributes creation

"""


class LockedClass():
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
