# 0x07-Rotate 2D Matrix

## Description

This directory contains a project focused on algorithms and matrix manipulation, specifically the rotation of a 2D matrix. The goal is to understand and implement the algorithm to rotate a given NxN 2D matrix 90 degrees clockwise in place.

## Contents

- **0. Rotate 2D Matrix**: Implement a function to rotate an NxN 2D matrix 90 degrees clockwise.

## Learning Objectives

- Understand the concept of matrix rotation.
- Implement an in-place algorithm to rotate a 2D matrix.
- Gain insights into matrix manipulation techniques.

## Requirements

- Python 3.x
- No external libraries required

## Getting Started

To get started with the project in this directory, follow these steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/majidied/alx-interview.git
   ```

2. Navigate to the `0x07-rotate_2d_matrix` directory:

   ```sh
   cd alx-interview/0x07-rotate_2d_matrix
   ```

3. Run the provided Python script to test the matrix rotation:

   ```sh
   python3 rotate_2d_matrix.py
   ```

## Usage

1. Ensure you have Python 3.x installed on your machine.
2. Implement the `rotate_2d_matrix` function in the `rotate_2d_matrix.py` file.
3. Run the script to test the function with different 2D matrix inputs.

## Example

Here is an example of how the function works:

```python
def rotate_2d_matrix(matrix):
    """
    Rotate the matrix 90 degrees clockwise in place
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last - (i - first)][first]
            matrix[last - (i - first)][first] = matrix[last][last - (i - first)]
            matrix[last][last - (i - first)] = matrix[i][last]
            matrix[i][last] = top

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
```

Output:

```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Contributing

We welcome contributions to improve and extend the functionality of this project. To contribute:

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Mohammed Majidi - [@Twitter](https://twitter.com/majidied) - <majidimajidi2003@gmail.com>

Project Link: [https://github.com/majidied/alx-interview/tree/main/0x07-rotate_2d_matrix](https://github.com/majidied/alx-interview/tree/main/0x07-rotate_2d_matrix)
