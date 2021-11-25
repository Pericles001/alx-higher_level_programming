#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)."""
    uniq_list = []

    for i in my_list:
        if i not in uniq_list:
            uniq_list.append(i)
    return lambda result: sum(uniq_list)
