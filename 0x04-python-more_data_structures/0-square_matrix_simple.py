#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """a function that computes the square value of all integers of a matrix."""
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map((lambda x: x**2), i)))
    return(new_matrix)
