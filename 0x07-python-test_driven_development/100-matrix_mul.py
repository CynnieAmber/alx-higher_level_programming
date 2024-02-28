#!/usr/bin/python3
""" Matrix multplication module """


def matrix_mul(m_a, m_b):
    """ matrix multplication function """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_b should contain only integers or floats")
    row_a = []
    row_b = []
    for row in m_a:
        row_a.append(len(row))
    if len(set(row_a)) != 1 and len(row_a) > 0:
        raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        row_b.append(len(row))
    if len(set(row_b)) != 1 and len(row_b) > 0:
        raise TypeError("each row of m_b must be of the same size")
    if row_a[0] != len(row_b):
        raise ValueError("m_a and m_b can't be multiplied")

    newlist = []
    newmatrix = []
    result = 0
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result += m_a[i][k] * m_b[k][j]
            newlist.append(result)
            result = 0
        newmatrix.append(newlist)
        newlist = []

    return newmatrix
