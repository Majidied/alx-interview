#!/usr/bin/python3
""" Rotate Matrix 90 deg """
from itertools import chain
import numpy as np


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (List[List]): The input matrix.

    Returns:
        None: The matrix is rotated in-place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return

    np.transpose(matrix)
    for row in matrix:
        row.reverse()
