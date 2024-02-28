#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
m_a = [[1, 2, 3],
        [4, 5, 6]]
m_b = [[7, 8],
        [9, 10],
        [11, 12]]

print(matrix_mul(m_a, m_b))
