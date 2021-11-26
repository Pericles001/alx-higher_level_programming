#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """computes the square value of all integers of a matrix using map"""
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
