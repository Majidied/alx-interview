# 0x0A. Prime Game

## Description

This directory contains solutions and explanations for the **Prime Game** problem, which is part of the **ALX Software Engineering Interview Preparation** curriculum.

## Problem Statement

Maria and Ben are playing a game with a set of consecutive integers starting from 1 up to and including `n`. They take turns choosing a prime number from the set and remove that number and all its multiples from the set. The game continues until a player cannot make a move, meaning no primes are left in the set. The player who cannot make a move loses the game.

## Objectives

- **Understand the rules** of the game and how the removal of primes affects the remaining set of numbers.
- **Develop a strategy** to determine the optimal moves and the conditions under which each player would win or lose.
- **Implement algorithms** to simulate the game and predict the outcome for different values of `n`.

## Files

- **`0-prime_game.py`**: This file contains the primary function to determine the winner of the game for a given set of rounds.
- **`main.py`**: A script to test the function with various inputs.
- **`README.md`**: This file, providing an overview of the problem and the contents of the directory.

## Concepts Covered

- Prime number identification
- Game theory basics
- Simulation of sequential decision-making
- Optimization strategies in algorithm design

## Game explanation

This problem involves a game played by Maria and Ben with a set of consecutive integers from 1 to \( n \). The rules are as follows:

1. **Starting Set**: The game begins with a set of consecutive integers \( \{1, 2, 3, \dots, n\} \).
2. **Prime Selection**: On each turn, the current player must choose a prime number from the set that hasn't been removed yet.
3. **Removal**: Once a player picks a prime number \( p \), that number \( p \) and all of its multiples \( p, 2p, 3p, \dots \) are removed from the set.
4. **Winning Condition**: The game continues until a player cannot make a move (i.e., there are no prime numbers left in the set). The player who cannot make a move loses the game.

### Steps to Approach the Problem

1. **Understand Prime Numbers**:
   - A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
   - Examples: 2, 3, 5, 7, 11, etc.

2. **Determine the Consequences of a Move**:
   - When a player picks a prime number \( p \), that prime and all its multiples are removed from the set. This drastically reduces the number of remaining possible moves.
   - For example, if \( n = 10 \) and Maria picks 2, she removes 2, 4, 6, 8, and 10 from the set.

3. **Identify Remaining Prime Numbers**:
   - After each turn, the remaining set will only have numbers that are not multiples of the primes already picked.
   - The number of remaining primes after each turn will determine whether a player has a move or not.

4. **Strategy**:
   - The game is heavily influenced by the order of play. The first player has the advantage of picking the smallest prime and removing more numbers.
   - The game continues until no primes are left to pick, and the player who cannot pick a prime loses.

### Example Scenario

Let's consider \( n = 10 \) to visualize the game:

- Initial set: \( \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\} \)
- **Maria's turn**: Maria picks the smallest prime, which is 2. She removes 2, 4, 6, 8, and 10. Remaining set: \( \{1, 3, 5, 7, 9\} \).
- **Ben's turn**: Ben picks the next smallest prime, which is 3. He removes 3, 9. Remaining set: \( \{1, 5, 7\} \).
- **Maria's turn**: Maria picks 5 (next prime) and removes it. Remaining set: \( \{1, 7\} \).
- **Ben's turn**: Ben picks 7 (last prime) and removes it. Remaining set: \( \{1\} \).
- **Maria's turn**: Maria cannot pick a prime number because there are no primes left. Thus, Maria loses.

### Conclusion

The outcome of the game depends on the number of prime numbers and the order of removal. The first player has an initial advantage, but the game's complexity lies in the strategic removal of primes to leave the opponent with no possible moves. The player who cannot make a move because no primes remain loses the game.

## Usage

You can test the solution by running the `main.py` file with the Python interpreter. Ensure you understand the rules and logic implemented within the solution to modify or extend the functionality for different game scenarios.

## Author

This project was completed as part of the ALX Software Engineering program. Contributions and suggestions are welcome!
