#!/usr/bin:env python3
"""
Rotate a Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2d Matrix
    """
    for i in range(len(matrix)):
        matrix[i].reverse()

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    matrix.reverse()
    for i in range(len(matrix)):
        matrix[i].reverse()
