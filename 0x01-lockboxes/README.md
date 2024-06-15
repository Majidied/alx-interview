# 0x01-lockboxes

## Introduction
The "0x01-lockboxes" project is a problem-solving exercise designed to test your algorithmic skills and understanding of data structures. The goal is to determine if all the boxes in a series can be unlocked given a certain initial set of keys.

## Learning Objectives
By completing this project, you will:
- Enhance your problem-solving abilities.
- Gain a deeper understanding of data structures such as arrays and lists.
- Learn to implement algorithms to traverse and manipulate these data structures.
- Improve your coding skills in Python by writing efficient and effective solutions.

## Project Description
You are given `n` locked boxes, each numbered sequentially from 0 to `n-1`. Each box may contain keys to other boxes. The task is to determine if you can unlock all the boxes, starting from box 0, using the keys available in each box.

### Requirements
- All keys are positive integers.
- Keys can only unlock boxes with corresponding integer numbers.
- The goal is to find out if all boxes can be unlocked.

## Files
- **0-lockboxes.py**: This file contains the primary implementation of the solution. The main function, `canUnlockAll`, checks if all the boxes can be unlocked.
- **main_0.py**: This file is a test script that runs multiple test cases against the `canUnlockAll` function to ensure it works correctly.

## Example
Given a list of boxes with their respective keys:
```python
boxes = [[1], [2], [3], [4], []]
```
- Box 0 contains a key to box 1.
- Box 1 contains a key to box 2.
- Box 2 contains a key to box 3.
- Box 3 contains a key to box 4.
- Box 4 is empty.

Starting from box 0, you can sequentially open all boxes. Hence, the function `canUnlockAll(boxes)` should return `True`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/0x01-lockboxes.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 0x01-lockboxes
   ```

## Usage
1. Implement the `canUnlockAll` function in the `0-lockboxes.py` file.
2. Run the test script to check if the function works as expected:
   ```bash
   python3 main_0.py
   ```

## Implementation Details
### canUnlockAll Function
The `canUnlockAll` function takes a list of lists as input, where each sublist represents a box and contains keys to other boxes. The function should return `True` if all boxes can be unlocked, otherwise `False`.

#### Algorithm
1. Initialize a list to keep track of unlocked boxes.
2. Start with box 0 as unlocked.
3. Use a stack to manage boxes to be checked.
4. For each box, unlock all boxes that its keys can open if they are not already unlocked.
5. Repeat until there are no more boxes to check.
6. If all boxes are unlocked, return `True`; otherwise, return `False`.

## Author
This project is maintained by Majidi Mohammed. Contributions, issues, and feature requests are welcome.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the algorithmic problem-solving community and various online resources that provided insights and examples used in this project.

---
