#!/usr/bin/python3
"""

A function that multiplies two matrices if possible

"""


def matrix_mul(m_a, m_b):
    """
    Args:
        m_a: first matrix
        m_b: second matrix

    Raises:
        TypeError: if either args is not list of lists
        TypeError: if all the elements in either args are
            not integers or floats
        TypeError: if the length of all the rows of either m_a
            or m_b are not equal
        ValueError: if either of the list is empty or if
            m_a and m_b cannot be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for ele in row:
            if (not isinstance(ele, int) and not isinstance(ele, float)):
                raise TypeError("m_a should contain only integers or floats")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for ele in row:
            if (not isinstance(ele, int) and not isinstance(ele, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []
    for i in range(len(m_a)):
        my_row = []
        for j in range(len(m_b[0])):
            product = 0
            for k in range(len(m_b)):
                product += m_a[i][k] * m_b[k][j] 
            my_row.append(product)
        m_c.append(my_row)
    return (m_c)
