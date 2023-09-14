#!/usr/bin/python3
"""
12-pascal_triangle
"""


def pascal_triangle(n):
    """
    Represents Pascal's Triangle of size n
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n):
        prev_row = triangle[-1]
        my_row = [1]
        for j in range(len(triangle) - 1):
            my_row.append(prev_row[j + 1] + prev_row[j])
        my_row.append(1)
        triangle.append(my_row)
    return triangle
