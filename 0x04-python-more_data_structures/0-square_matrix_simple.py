#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    return list([ele * ele for ele in row] for row in matrix)
