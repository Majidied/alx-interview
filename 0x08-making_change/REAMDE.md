# 0x08. Making Change

This directory contains the solution to the "Making Change" interview question, which is part of the `alx-interview` repository. The problem is a classic dynamic programming challenge that involves finding the minimum number of coins needed to make a specific amount of change.

## Project Description

In this project, you are given a pile of coins of different values, and your goal is to determine the fewest number of coins needed to meet a given amount of change. If the change cannot be made with the given coin denominations, you should return `-1`.

## Files

- **0-making_change.py**: The main Python script containing the solution to the problem.

## Problem Statement

Given a list of integers representing coin denominations and a single integer representing the amount of change, write a function that determines the minimum number of coins needed to make that amount of change. If it's not possible to make the change with the given coin denominations, the function should return `-1`.

### Function Prototype

```python
def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to meet a given amount of change.
    
    Parameters:
    coins (List[int]): A list of integers representing the available coin denominations.
    total (int): The total amount of change needed.
    
    Returns:
    int: The minimum number of coins needed to make the change, or -1 if it's not possible.
    """
```

### Example

```python
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3 (5 + 5 + 1)
```

### Constraints

- You may assume that the total amount is a non-negative integer.
- The list of coin denominations will contain at least one coin of value greater than `0`.

## Approach

The solution employs a dynamic programming approach to solve the problem efficiently. Here's a brief explanation of the algorithm:

1. **Initialization**: Create a list `dp` where `dp[i]` represents the minimum number of coins needed to make `i` amount of change. Initialize `dp[0]` to `0` because no coins are needed to make a total of `0`. Initialize all other values in `dp` to infinity (or a sufficiently large number).
2. **Dynamic Programming**: Iterate through each coin and update the `dp` list by considering each amount from the coin value to the total amount. For each amount, update the `dp` value to the minimum of its current value or `dp[amount - coin] + 1`.
3. **Result**: If `dp[total]` is still infinity after processing, it means the change cannot be made with the given coin denominations, so return `-1`. Otherwise, return `dp[total]`.

## How to Use

To use the `makeChange` function, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/majidied/alx-interview.git
    ```

2. Navigate to the `0x08-making_change` directory:

    ```sh
    cd alx-interview/0x08-making_change
    ```

3. Run the script with your desired input:

    ```sh
    python3 0-making_change.py
    ```

## Author

Mohammed Majidi - [GitHub](https://github.com/majidied)
