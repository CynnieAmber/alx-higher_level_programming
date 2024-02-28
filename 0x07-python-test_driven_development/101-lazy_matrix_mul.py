#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
    m_a (list of lists of ints/floats): The first matrix.
    m_b (list of lists of ints/floats): The second matrix.
    """
    A1 = np.array(m_a)
    A2 = np.array(m_b)
    return (np.matmul(m_a, m_b))
    # return A1.dot(A2)
