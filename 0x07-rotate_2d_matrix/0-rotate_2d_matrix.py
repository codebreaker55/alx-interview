#!/usr/bin/python3
"""a module to rotate n x n 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotates 2D matrix 90 degrees clockwise
    Matrix is edited in-place
    args:
        matrix (list of lists): 2D matrix to rotate
    """
    m_size = len(matrix)

    # transpose the matrix
    for r in range(m_size):
        for col in range(r, m_size):
            matrix[r][col], matrix[col][r] = matrix[col][r], matrix[r][col]

    # reverse each row
    for r in range(m_size):
        matrix[r].reverse()
