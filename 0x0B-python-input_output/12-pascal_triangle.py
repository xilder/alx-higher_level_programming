#!/usr/bin/python3
"""creates a list of lists of integers that represent
    the Pascal Triangle
"""


def pascal_triangle(n):
    if (n <= 0):
        return []

    triangle = [[1]]
    for i in range(n):
        my_row = [1]
        if len(triangle) > 1:
            for j in range(1, len(triangle)):
                value = prev_row[j - 1] + prev_row[j]
                my_row.append(value)
        my_row.append(1)
        prev_row = my_row
        triangle.append(my_row)
    return triangle

