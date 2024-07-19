#!/usr/bin/python3
""" Rotate Matrix 90 deg """
from itertools import chain


from typing import List


def transpose2(M: List[List]) -> List[List]:
    """Matrix Transposition

    Args:
        M (List[List]): original matrix

    Returns:
        List[List]: transposing matrix
    """
    n = len(M[0])
    L = list(chain(*M))
    return [L[i::n] for i in range(n)]


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (List[List]): The input matrix.

    Returns:
        None: The matrix is rotated in-place.
    """
    if not matrix or not matrix[0]:
        return

    matrix[:] = transpose2(matrix)
    for row in matrix:
        row.reverse()
