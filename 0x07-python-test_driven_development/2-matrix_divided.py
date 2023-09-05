#!/usr/bin/python3
"""

Returns a new matrix where element is a result of the
previous element divided by div

new_matrix[i][j] = matrix[i][j] / div

"""


def matrix_divided(matrix, div):
    """Returns a new matrix

    Args:
        matrix: a list of lists
        div: the denominator for the matrix

    Returns:
        a new matrix as where
        new_matrix[i][j] = matrix[i][j] / div

    Raises:
        TypeError: if the matrix is not a list of lists,
            if the lists are of different lengths,
            if any of the elements is not an int or a float,
            if the div is not an int or a float
        ZeroDivisionError: if div is a zero
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of "
                            "lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if (not isinstance(i, int) and not isinstance(i, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
