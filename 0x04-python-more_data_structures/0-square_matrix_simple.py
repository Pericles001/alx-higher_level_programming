#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """a function that computes the square value of all integers of a matrix."""
    new_matrix = []
    for i in matrix:
        new_matrix.append([x**2 for x in i])
    return(new_matrix)
