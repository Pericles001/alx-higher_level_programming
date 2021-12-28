#!/usr/bin/python3
"""Module that represent base model class"""


class Base:
    """Base model representation
    
        Attributes:
            __nb__objects (int): number of bases
    """

    __nb__objects = 0

    def __init__(self, id=None):
        """
        Initialize class
        
            Args:
                id (int): The identity of the new base
        """

    if id is not None:
        self.id = id
    else:
        __nb__objects += 1
        self.id = Base.__nb__objects



