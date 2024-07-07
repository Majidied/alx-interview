#!/usr/bin/python3
""" N queens problem """
import sys


def is_safe(board, row, col):
    """ Check if a queen can be placed on board[row][col] """
    for i in range(col):
        if board[i] == row or board[i] == row - col + i or board[i] == row + col - i:
            return False
    return True


def solve(board, col):
    """ Solve N queens problem """
    n = len(board)
    if col == n:
        print(str([[i, board[i]] for i in range(n)]))
        return
    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve(board, col + 1)
            board[col] = -1


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)
board = [-1 for i in range(N)]
solve(board, 0)
