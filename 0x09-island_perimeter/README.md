# 0x09. Island Perimeter

## Description

This directory contains solutions to problems related to finding the perimeter of an island in a grid. The main objective is to implement an algorithm that calculates the perimeter of an island represented by a 2D grid. The grid cells are either water or land, and the island is formed by connecting adjacent land cells horizontally or vertically. The grid is completely surrounded by water, and there is exactly one island (or none).

## Learning Objectives

- Understand how to traverse 2D grids.
- Learn to implement algorithms for calculating perimeter.
- Practice handling edge cases in grid-based problems.

## Files

- `0-island_perimeter.py`: A Python function that takes a grid (list of lists) and returns the perimeter of the island.

## Function Prototype

```python
def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    
    :param grid: List of list of integers where 0 represents water and 1 represents land.
    :return: Integer representing the perimeter of the island.
    """
```

## Example

```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/majidied/alx-interview.git
    ```

2. Navigate to the directory:
    ```bash
    cd alx-interview/0x09-island_perimeter
    ```

3. Run the Python script:
    ```bash
    python3 0-island_perimeter.py
    ```

## Author

- Mohammed Majidi

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
