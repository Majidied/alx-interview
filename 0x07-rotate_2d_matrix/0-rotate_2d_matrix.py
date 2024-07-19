#!/usr/bin/python3
""" Rotate Matrix 90 deg """


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if not isinstance(
        matrix,
        list) or len(matrix) == 0 or not all(
        isinstance(
            row,
            list) for row in matrix):
        return
    if not all(len(row) == len(matrix) for row in matrix):
        return

    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
