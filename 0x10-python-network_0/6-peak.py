#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    if len(list_of_integers) > 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] > list_of_integers[-2]:
            return list_of_integers[-1]
        for i in range(1, len(list_of_integers) - 1):
            if (list_of_integers[i] > list_of_integers[i - 1]
                    and list_of_integers[i] > list_of_integers[i + 1]):
                return list_of_integers[i]
    return None
