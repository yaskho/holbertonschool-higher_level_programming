#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all elements
of a matrix by a given number and returns a new matrix with the results
rounded to 2 decimal places.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimal places."""

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(val / div, 2) for val in row] for row in matrix]
