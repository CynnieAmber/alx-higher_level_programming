#!/usr/bin/python3
""" Matrix division modeule """


def matrix_divided(matrix, div):
    """ matrix division function """
    if matrix is None:
        raise TypeError("matrix must"
                        " be a matrix (list of lists) of integers/floats")
    # if all(not row for row in matrix):
        # return []
    if type(div) is not int and (type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must"
                        " be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    rowlen = []
    for row in matrix:
        rowlen.append(len(row))
    if len(set(rowlen)) != 1 and len(rowlen) > 0:
        raise TypeError("Each row of the matrix must have the same size")
    result = [[round(x / div, 1) if x % div == 0 else round(x / div, 2)
               for x in row] for row in matrix]
    return result
