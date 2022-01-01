#!/usr/bin/python3
"""Module that represent base model class"""
import json
import csv
from os import write
import turtle

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
         Base.__nb__objects += 1
         self.id = Base.__nb__objects



    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)


    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile/write(Base.to_json_string(list_dicts))

