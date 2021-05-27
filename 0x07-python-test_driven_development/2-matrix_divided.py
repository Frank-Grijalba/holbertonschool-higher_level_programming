#!/usr/bin/python3
"""
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Divide each item of a matrix
    """

    e = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError(e)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(e)
        for value in row:
            if type(value) not in [float, int]:
                raise TypeError(e)

    len_row = []
    for row in matrix:
        len_row.append(len(row))
    item = len_row[0]
    for i in len_row:
        if item != i:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(value / div, 2) for value in row] for row in matrix]

    return new_matrix
