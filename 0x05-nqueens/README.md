# 0x05. N Queens

## Description
This directory contains a solution to the N Queens problem, a classic algorithmic challenge. The objective is to place N chess queens on an N×N chessboard so that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Files
- `0-nqueens.py`: This is the main executable file that contains the solution to the N Queens problem.

## Usage
To execute the program, run the following command in your terminal:

```bash
./0-nqueens.py N
```

where `N` is the size of the board and the number of queens to be placed. The program will print every possible solution to the problem, where each solution is represented by a list of positions. Each position is in the format `[row, column]`.

## Example
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Algorithm
The solution uses a backtracking approach to place queens on the board:
1. Start in the leftmost column.
2. If all queens are placed, return true.
3. Try all rows in the current column. For every row, check if the queen can be placed:
   - If placing the queen in [row, column] does not lead to a solution, remove the queen and try the next row.
4. If placing the queen in any row leads to a solution, return true.
5. If no row can lead to a solution, return false.

## Author
- [Mohammed Majidi](https://github.com/majidied)
