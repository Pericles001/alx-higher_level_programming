#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """returns a list with all values multiplied"""
    """ by a number without using any loops."""
    return list(map(lambda x: x * number, my_list))
